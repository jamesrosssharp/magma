
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

        # Find the point where vinn crosses vinp

        cross_point = 0
        for i in range(0, plot['num_points']):
            if plot['data']['v(inn)'][i] > plot['data']['v(inp)'][i]:
                cross_point = i
                break
        out_point = 0
        for i in range(100, plot['num_points']):
            if plot['data']['v(comp_out)'][i] < 0.5:
                out_point = i
                break
    
        if 0:
            plt.plot(plot['data']['v(inn)'], label = 'vinn')
            plt.plot(plot['data']['v(inp)'], label = 'vinp')
            plt.plot(plot['data']['v(comp_out)'], label='comp_out')
            plt.plot(plot['data']['v(clk)'], label='clk')
            plt.plot(plot['data']['v(x1.x2.vlat_plus)'], label = 'vlatp')
            plt.plot(plot['data']['v(x1.x2.vlat_minus)'], label = 'vlatm')
            plt.legend()
            plt.show()

        
        cross_time = plot['data']['time'][cross_point] 
        out_time = plot['data']['time'][out_point]

        pd = out_time - cross_time

        delay.append(pd)
        vinn.append(plot['data']['v(inn)'][0])
        offset.append(plot['data']['v(inn)'][out_point] - plot['data']['v(inp)'][out_point])

        # Skip over startup transients
        power = np.abs(plot['data']['v(vdd)']*plot['data']['i(vvdd)'])[100:]
        power_min.append(np.min(power))
        power_max.append(np.max(power))
        power_av.append(np.mean(power))


        #plt.plot(plot['data']['time'][100:], power)
        #plt.show()

        #print("%d, " % n, end="")
        print("{:1.2g}, {:1.2g}, {:1.2g}, {:1.2g}, {:1.2g}, {:1.2g}, ".format(plot['data']['v(temperat)'][0], 
        plot['data']['v(inp)'][0], plot['data']['v(vdd)'][0], cross_time, out_time, pd), end="") 
        

        if pd < 30e-9 and pd >= 0:
            vdd.append(plot['data']['v(vdd)'][0])
            temp.append(plot['data']['v(temperat)'][0])
            vcm.append(plot['data']['v(inp)'][0])
            pds.append(pd)
            print("OK")
        else:
            if 0:
                plt.plot(plot['data']['v(inn)'])
                plt.plot(plot['data']['v(inp)'])
                plt.plot(plot['data']['v(comp_out)'])
                plt.show()
        
            print("Failed")
            failures.append((plot['data']['v(temperat)'][0],
            plot['data']['v(inp)'][0], plot['data']['v(vdd)'][0]))

    # Print common mode voltage range
    print(" Working Common mode range: {:1.2g} - {:1.2g} V".format(np.min(np.array(vcm)), np.max(np.array(vcm))))

    # Print temperature range
    print("Working Temperature range: {:.2f} - {:.2f} Deg C".format(np.min(np.array(temp)), np.max(np.array(temp))))

    # Print vdd range 
    print("Working Supply voltage range: {:1.2g} - {:1.2g} V".format(np.min(np.array(vdd)), np.max(np.array(vdd))))

    # Print min, max and average power
    print("Power consumption: min {} max {} av {} W".format(np.min(np.array(power_min)), np.max(np.array(power_max)), np.mean(np.array(power_av))))

    print ("Average propagation delay: {} s worst: {} s".format(np.mean(pds), np.max(pds)))

    print()

    print("Failures: ")
    print(failures)

#for corner in ["tt", "ss", "fs", "sf", "ff"]:
for corner in ["tt", "ss", "sf"]:
    load_corner(corner)

plt.figure(figsize=(8, 6))
h, xedges, yedges, image = plt.hist2d(vinn, delay, bins=100, cmap='viridis')

# Add colorbar and labels
plt.colorbar(label='Count in bin')
plt.xlabel('Common mode')
plt.ylabel('Delay')
plt.title('2D Histogram (Density Heatmap)')
plt.show()

plt.figure(figsize=(8, 6))
h, xedges, yedges, image = plt.hist2d(vinn, offset, bins=100, cmap='viridis')

# Add colorbar and labels
plt.colorbar(label='Count in bin')
plt.xlabel('Common mode')
plt.ylabel('Offset')
plt.title('2D Histogram (Density Heatmap)')
plt.show()

