from mpmath import sqrt, mp


def calc_circular_eq_coords(psi, En, Lz, aa, slr, M=1):
    # lam_psi is used to cross check with circular orbits in BHPTK
    # lam_psi = (psi / (sqrt(1 - En**2 + 3*(1 - En**2) + 2*(1 - En**2 - 1/slr) + 
    #            (aa**2*(1 - En**2) + Lz**2)/slr**2 - 4/slr)*slr))
    # print(lam_psi)

    aa2 = aa * aa
	slr2 = slr * slr
	x = Lz - aa * En
	x2 = x * x

    Vr = aa2 + x2 + 2 * aa * x * En - 6 * M * x2 / slr
    Vphi = x + aa * En - 2 * M * x / slr
    Vt = aa2 * En - 2 * aa * M * x / slr + En * slr2
    J = 1 - 2 * M / slr + aa2 / slr2
    denom = J * sqrt(Vr)
	t = Vt / denom * psi
    phi = Vphi / denom * psi
    r = slr
	theta = mp.pi / 2
    return t, r, theta, phi
