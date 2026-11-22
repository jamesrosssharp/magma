
import numpy as np
from matplotlib import pyplot as plt

import scipy

from load_spice import load_spice

delay = []
vinn = []
offset = []

def load_corner(corner):

    plots = load_spice.load_spice("build/{}.raw".format(corner))

    print("")
    print("")
    print("Results for corner {}".format(corner))


    plot1 = plots[1]
    print(plot1['vars'])

    failures = []

    vdd = []
    vcm = []
    temp = []

    power_min = []
    power_max = []
    power_av  = []
    pds = []

    for n, plot in enumerate(plots[1:]):

        j = 0
        for t in plot['data']['time']:
            if t > 3e-6:
                break
            j += 1

        if 1:
            
            plt.plot(plot['data']['time'][j:], plot['data'][f'v(inp)'][j:] + 2.0 * 1, label=f'VINP')
            plt.plot(plot['data']['time'][j:], plot['data'][f'v(inn)'][j:] + 2.0 * 2, label=f'VINN')
            for i in range(0,10):
                if i < 8:
                    lab = f"uio_out[{i}]"
                else:
                    lab = f"uo_out[{i - 8}]"

                plt.plot(plot['data']['time'][j:], plot['data'][f'v(out{i})'][j:] + 2.0 * (i+3), label=lab)
            #plt.plot(plot['data']['v(x1.x2.vlat_plus)'], label = 'vlatp')
            #plt.plot(plot['data']['v(x1.x2.vlat_minus)'], label = 'vlatm')
            plt.yticks([])
            plt.title(f"Waveforms for corner {corner}")
            plt.xlabel(f"Time, s")
            plt.legend()
            plt.show()

        
for corner in ["tt", "ss", "fs", "sf", "ff"]:
#for corner in ["tt"]: #, "ss", "sf"]:
    load_corner(corner)

