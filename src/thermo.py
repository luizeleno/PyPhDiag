import numpy as np

'''
    CALPHAD phase models
'''


class sol_phase:
    '''
        Solution phases
    '''
    def __init__(self, label, Gref, L, R=1.987):
        self.label = label
        self.L = np.array(L)
        self.Gref = np.array(Gref)
        self.R = R
        self.kind = 'sol'

    def xlnx(self, x):
        s = x * np.log(x)
        return np.nan_to_num(s)

    def Sid(self, x):
        xA = 1 - x
        xB = x
        f = self.xlnx(xA) + self.xlnx(xB)
        return -self.R * f

    def Gex(self, x, T):
        xA = 1 - x
        xB = x
        c = xA - xB
        cp = 1
        p = 0
        for n in range(self.L.size):
            Ln = eval(self.L[n])
            p += Ln * cp
            cp *= c
        return p * xA * xB

    def G(self, x, T):
        Gex = self.Gex(x, T)
        GA = eval(self.Gref[0])
        GB = eval(self.Gref[1])
        Gref = (1 - x) * GA + x * GB
        return Gref + Gex - T * self.Sid(x)


class stq_phase:
    '''
        Stoichiometric phases
    '''

    def __init__(self, label, n, Gref, L):
        self.label = label
        self.xA = n[0] / (n[0] + n[1])
        self.xB = 1 - self.xA
        self.Gref = np.array(Gref)
        self.L = np.array(L)
        self.kind = 'stq'

    def Gex(self, T):
        c = self.xA - self.xB
        cp = 1
        p = 0
        for n in range(self.L.size):
            Ln = eval(self.L[n])
            p += Ln * cp
            cp *= c
        return p * self.xA * self.xB

    def G(self, T):
        GA = eval(self.Gref[0])
        GB = eval(self.Gref[1])
        Gref = self.xA * GA + self.xB * GB
        return Gref + self.Gex(T)
