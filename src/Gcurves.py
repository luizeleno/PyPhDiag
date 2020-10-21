import numpy as np
import convexhull as ch
import matplotlib.pyplot as plt
import markers
import MoZr

# importing system data
MoZr = MoZr.data()

# Calculation of free energy curves

Tmin, Tmax, dT = 1200, 3000, 50  # temperature limits for the phase diagram

Nx, tol = 50, 1e-6  # number of compositions, first composition
x = np.linspace(tol, 1-tol, Nx+1)  # composition array
dx = x[1] - x[0]

# initializing graphics
fig = plt.figure()
ax = fig.add_subplot(111)

# creating G curves
Tlist = np.arange(Tmin, Tmax+dT, dT)
for T in Tlist:

    print(f'T = {T} K')

    # figure name
    figfile = f'../example/PhD/MoZr-T{T}.png'

    # preparing graphics
    plt.cla()
    ax.set_xlim([0, 1])
    ax.set_xlabel(r'$x_\mathrm{Zr}$')
    ax.set_ylabel(r'$G_m$ (J/mol)')
    ax.text(0.03, .95, f'$T={T}$ K', transform=ax.transAxes)

    # calculating hull and tielines
    Gdata, hull, vertices = ch.hull(x, T, MoZr)
    tielines, nt = ch.tielines(vertices, Gdata, dx)

    # showing free energy curves
    mkr = markers.markers()
    for phase in MoZr:
        if phase.kind == 'sol':
            ax.plot(x, phase.G(x, T), next(mkr), markersize=4,
                    label=phase.label)
        elif phase.kind == 'stq':
            ax.plot(phase.xB, phase.G(T), 'o', label=phase.label, markersize=8)

    # showing tielines
    for i in range(0, nt, 2):
        ax.plot(Gdata[tielines[i:i+2], 0], Gdata[tielines[i:i+2], 1],
                'b-o', markersize=6)
    ax.plot([], [], 'b-o', label='tielines')  # legend

    # showing convex hull
    ax.plot(hull[:, 0], hull[:, 1], 'k.', label='convex hull')

    plt.legend()
    fig.tight_layout()
    plt.savefig(figfile)
