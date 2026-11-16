
import numpy as np
from matplotlib import pyplot as plt

from load_spice import load_spice

from scipy.fft import rfft, rfftfreq
from scipy.signal.windows import hann

DEBUG_PLOT = False


def load_corner(corner):

    plots = load_spice.load_spice("build/{}.raw".format(corner))

    print("")
    print("")
    print("Results for corner {}".format(corner))

    print("run,corner,avg power,avg current,in_freq,temp,vdd,test_pass")

    plot1 = plots[1]
#    print(plot1['vars'])

    failures = []

    vdd = []
    vcm = []
    temp = []

    power_min = []
    power_max = []
    power_av  = []
    pds = []

    for n, plot in enumerate(plots[1:]):

        if DEBUG_PLOT:
            plt.plot(plot['data']['v(vout)'], label = 'vout')
            plt.plot(plot['data']['v(vin)'], label = 'vin')
            #plt.plot(plot['data']['v(pwm_in)'])
            plt.legend()
            plt.show()

        # Plot fft of v(vout)

        # 1. Load exported SPICE data (e.g., tab- or comma-separated with header)
        # Adjust 'delimiter' and 'skiprows' to match your LTspice/ngspice export
        
        for i in range(0, len(plot['data']['time'])):
            if plot['data']['time'][i] > 3e-6:
                break

        t_raw = plot['data']['time'][i:]
        v_raw = plot['data']['v(vout)'][i:]
        vin_raw = plot['data']['v(vin)'][i:]
        in_freq = plot['data']['v(freq_v)'][0]

        # 2. Interpolate onto a uniform time grid
        # Choose N as a power of 2 or match your desired Nyquist frequency
        N = 1024 
        t_uniform = np.linspace(t_raw[0], t_raw[-1], N, endpoint=False)
        v_uniform = np.interp(t_uniform, t_raw, v_raw)
        vin_uniform = np.interp(t_uniform, t_raw, vin_raw)

        # Calculate uniform time step (dt)
        dt = t_uniform[1] - t_uniform[0]

        # 3. Remove DC offset and apply a window function (reduces spectral leakage)
        v_ac = v_uniform - np.mean(v_uniform)
        vin_ac = vin_uniform - np.mean(vin_uniform)
        window = hann(N)
        v_windowed = v_ac  * window
        vin_windowed = vin_ac  * window

        # 4. Compute the single-sided FFT and frequency bins
        yf = rfft(v_windowed)
        xf = rfftfreq(N, d=dt)

        yf2 = rfft(vin_windowed)


        # Scale amplitude (compensating for the Hann window coherent gain of 0.5)
        amplitude = (2.0 / N) * np.abs(yf) / 0.5
        amplitude_db = 20 * np.log10(amplitude + 1e-12)  # Avoid log(0)

        amplitude2 = (2.0 / N) * np.abs(yf2) / 0.5
        amplitude_db2 = 20 * np.log10(amplitude2 + 1e-12)  # Avoid log(0)

        if DEBUG_PLOT:

            # 5. Plot the spectrum
            fig, (ax1) = plt.subplots(1, 1, figsize=(10, 7))

            # Decibel (dBV) Plot
            ax1.plot(xf, amplitude_db, label = 'VOUT')
            ax1.plot(xf, amplitude_db2, label = 'VIN')
            ax1.set_title(f'SPICE Signal FFT (Logarithmic / dBV), freq = {in_freq:0.2e} ')
            ax1.set_xlabel('Frequency [Hz]')
            ax1.set_ylabel('Magnitude [dBV]')
            ax1.set_ylim(-100, 3)
            ax1.legend()
            ax1.grid(True)

            plt.tight_layout()
            plt.show()

        test_pass = False

        if (np.argmax(amplitude) == np.argmax(amplitude2)):
            test_pass = True
              
        # Skip over startup transients
        power = np.abs(plot['data']['v(vdd)']*plot['data']['i(vvdd)'])[100:]
        power_min.append(np.min(power))
        power_max.append(np.max(power))
        power_av.append(np.mean(power))

        vdd = plot['data']['v(vdd)'][0]
        temp = (plot['data']['v(temperat)'][0])
        current = np.abs(plot['data']['i(vvdd)'][100:])   


        print(f"{n},{corner},{np.mean(current):0.2e},{np.mean(power):0.2e},{in_freq:0.2e},{temp:0.2e},{vdd:0.2e},{test_pass}")


#for corner in ["tt", "ss", "fs", "sf", "ff"]:
for corner in ["tt"]:
    load_corner(corner)


