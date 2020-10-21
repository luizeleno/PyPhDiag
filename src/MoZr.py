import thermo

'''
    Data from
    Kaufman, L., & Bernstein, H. (1970). Computer calculation of phase
    diagrams, with special reference to refractory metals.
    Academic Press,  New York.
'''


def data():
    GMoLiq = '0'
    GZrLiq = '0'

    GMoBCC = '-5800+2*T'
    GZrBCC = '-4250+2*T'

    GMoHCP = '-3800+2*T'
    GZrHCP = '-5280+2.9*T'

    L0Liq = '1512'
    L0BCC = '6551'
    L0HCP = '8981'

    cLaves = [2, 1]
    GMoLaves = GMoHCP
    GZrLaves = GZrHCP
    L0Laves = '-16488'

    # PHASES
    phases = []
    phases.append(thermo.sol_phase('liq', [GMoLiq, GZrLiq], [L0Liq]))
    phases.append(thermo.sol_phase(r'$BCC$', [GMoBCC, GZrBCC], [L0BCC]))
    phases.append(thermo.sol_phase(r'$HCP$', [GMoHCP, GZrHCP], [L0HCP]))
    phases.append(thermo.stq_phase(r'$Laves$', cLaves,
                                   [GMoLaves, GZrLaves], [L0Laves]))

    return phases
