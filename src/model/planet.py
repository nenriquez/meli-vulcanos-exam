from model.celestial_body import CelestialBody
from model.geometry import RADIO

class Planet(CelestialBody):

    # angular velocity in degrees per day
    angular_vel = None


    def __init__(self, name, coor, angular_velocity):
        """
        Creates new planet.

        :param name: spawn name
        :param coor: spawn coordinates
        :param angular_velocity: planet's angular velocity relative to (0, 0)
        """
        CelestialBody.__init__(self, name, coor)
        self.angular_vel = angular_velocity

    def grownup(self, delta_days):
        self.coor.plus_angle(delta_days * self.angular_vel)

    def get_age_days(self):
        return round(RADIO / self.angular_vel)



