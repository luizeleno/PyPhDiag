import numpy as np
import scipy.spatial as spa


def hull(x, T, data):

    # getting minimal G for each x - solution phases
    Fgy = [fase.G(x, T) for fase in data if fase.kind == 'sol']
    Gmin = np.amin(Fgy, axis=0)
    Gmin = np.column_stack((x, Gmin))

    # adding stoichiometric phases
    for fase in data:
        if fase.kind == 'stq':
            point = [[fase.xB, fase.G(T)]]
            Gmin = np.append(Gmin, point, axis=0)

    # ordering array by composition
    Gmin = Gmin[np.argsort(Gmin[:, 0])]

    # getting convex hull for solution phases
    hull = spa.ConvexHull(Gmin)

    # shifting first position to end
    vertices = np.roll(hull.vertices, -1)

    # separating points belonging to hull
    points = hull.points[vertices, :]

    return Gmin, points, vertices


def tielines(vertices, Gdata, dx, TOL=1e-8):

    # getting differences in vertices array
    t = np.diff(vertices)
    t = np.where(t > 1)[0]  # filtering only diffs > 1

    tielines = []  # initializing tielines list
    for i in t:
        # checking for tielines based on dx + TOL
        if Gdata[vertices[i + 1], 0] - Gdata[vertices[i], 0] > dx + TOL:
            tielines.append(vertices[i])
            tielines.append(vertices[i + 1])

    nt = len(tielines)

    return tielines, nt
