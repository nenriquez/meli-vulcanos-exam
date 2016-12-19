from model.celestial_body import CelestialBody
from model.geometry import Polar

SUN_NAME = "Sun"


class Sun(CelestialBody):

    def __init__(self):
        """
        Creates new planet.

        :param name: spawn name
        :param coor: spawn coordinates
        :param angular_velocity: planet's angular velocity relative to (0, 0)
        """
        CelestialBody.__init__(self, SUN_NAME, Polar(0, 0))

    def grownup(self, delta_days):
        # nothing to do for now
        pass
