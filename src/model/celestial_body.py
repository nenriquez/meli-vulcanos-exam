from exception.exceptions import VirtualMethodException


class CelestialBody:

    # polar coordinates
    coor = None

    # planet identifier
    name = ""


    def __init__(self, name, coor):
        """
        Creates new planet.

        :param name: spawn name
        :param coor: spawn polar coordinates
        :param angular_velocity: planet's angular velocity
        """
        self.name = name
        self.coor = coor


    """
    Increase celestial bodie's days of life
    :param: delta_days (int): time to growup in days
    """
    def grownup(self, delta_days):
        raise VirtualMethodException("grownup")