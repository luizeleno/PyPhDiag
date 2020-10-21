import numpy as np
import convexhull as ch
import matplotlib.pyplot as plt
import MoZr

MoZr = MoZr.data()  # loading system data

Tmin, Tmax = 500, 3000  # temperature limits for the phase diagram

# initializing graphics
fig = plt.figure()
ax = fig.add_subplot(111)

# lists of precision parametes to consider
dTlist = [20, 10, 5, 1, .5]
Nxlist = [50, 100, 500, 1000, 5000, 10000]

# starting to generate figures
for dT in dTlist:
    for Nx in Nxlist:

        # starting graph
        plt.cla()
        ax.set_xlim([0, 1])
        ax.set_ylim([Tmin, Tmax])
        ax.set_xlabel(r'$x_\mathrm{Zr}$')
        ax.set_ylabel(r'$T$ (K)')

        # figure name
        figfile = f'../example/PhD/MoZr-dT{dT}-Nx{Nx:05d}.png'
        print(figfile)

        Temps = np.arange(Tmin, Tmax + dT, dT)  # temperature array

        tol = 1e-6  # first composition (to avoid log(0) calculation)
        x = np.linspace(tol, 1 - tol, Nx + 1)  # composition array
        dx = x[1] - x[0]

        # starting calculations
        for T in Temps:

            if T % 250 == 0:  # progress indicator
                print(f'T = {T} K')

            # calculating hull and tielines
            Gdata, hull, vertices = ch.hull(x, T, MoZr)
            tielines, nt = ch.tielines(vertices, Gdata, dx)

            # adding points to phase diagram
            ax.plot(Gdata[tielines, 0], [T] * nt, 'k.', markersize=1)

        fig.tight_layout()
        plt.savefig(figfile)
