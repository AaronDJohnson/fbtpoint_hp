from mpmath import mp, mpf
from geodesic.functions import calc_constants
from geodesic.functions import coordinates
from geodesic.functions import mino_coords


class Orbit:
    """
    Stores orbital parameters and contains methods to do stuff with
    these parameters.
    """
    def __init__(self, aa, slr, ecc, x, digits):
        self.aa = aa
        self.slr = slr
        self.ecc = ecc
        self.x = x
        self.digits = digits


    def geo_coords(self, psi=None, mino_t=None):
        if psi is not None:
            self.t, self.r, self.theta, self.phi = coordinates(psi, self.aa, self.slr, self.ecc, self.x, self.digits)
        elif psi is None and mino_t is not None:
            self.t, self.r, self.theta, self.phi = mino_coords(mino_t, self.aa, self.slr, self.ecc, self.x, self.digits)
        return self.t, self.r, self.theta, self.phi
