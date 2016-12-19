from model.geometry import Polar, Rect
from model.planet import Planet
from model.sun import Sun

class CelestialBodies:
    FERENGI = Planet("ferengi", Polar(500, 45), -1)
    BETASOIDE = Planet("betasoide", Polar(2000, 90), -3)
    VULCANO = Planet("vulcano", Polar(1000, 270), 5)
    SUN = Sun()


class PlanetaryWeather:
    DROUGHT_SEASON = 0  # is never rain season
    WET_SEASON = 1  # its rain a lot
    OTP_SEASON = 2  # optimal temp an pleasure season
    NORMAL_SEASON = 3  # nothing special


class PlanetarySystem:

    def __init__(self):
        self._sun = CelestialBodies.SUN
        self._days_old = 0
        self._longer_age_days = 0
        self._planets = [CelestialBodies.FERENGI, CelestialBodies.BETASOIDE, CelestialBodies.VULCANO]
        self._celestial_bodies = self._planets + [CelestialBodies.SUN]

    def _get_planet_cartesians(self):
        """
        :return: a list of cartesian coordinates of planets
        """
        return [p.coor.to_cartesian() for p in self._planets]

    def _get_planet_polars(self):
        """
        :return:  a list of polar coordinates of planets
        """
        return [p.coor for p in self._planets]

    def grownup(self, delta_days):
        """
        Increase the system age days in delta_days days.

        :param delta_days: amount of days that the system's age is going to be incremented.
        :return: None
        """
        self._days_old += delta_days

        for body in self._celestial_bodies:
            body.grownup(delta_days)

    def get_today_weather(self):
        """
        Verify the system status and return calculate weather based on his celestial bodies position.

        :return: PlanetaryWeather enum value that represent today's weather.
        """
        if self.is_drought_season():
            return PlanetaryWeather.DROUGHT_SEASON

        if self.is_opt_season():
            return PlanetaryWeather.OTP_SEASON

        if self.is_wet_season():
            return PlanetaryWeather.WET_SEASON

        return PlanetaryWeather.NORMAL_SEASON

    def has_full_alignment(self):
        """
        :return: true if there is alignment between all planets and the sun.
        """
        # if planets have the same angle then are alignment among them and the sun
        # p1, p2, p3 = self._get_planet_polars()
        # TODO: revisar pq esto no funciona:
        # return (p1.radians == p2.radians or math.fabs(p1.radians - p2.radians) == math.pi) \
        #             and (p1.radians == p3.radians or math.fabs(p1.radians - p3.radians) == math.pi)

        p1, p2, p3 = self._get_planet_cartesians()
        return Rect(p1, p2).contain(p3) and Rect(p1, p2).contain(self._sun.coor.to_cartesian())

    is_drought_season = has_full_alignment

    def has_planetary_alignment(self):
        """
        :return true if there is alignment between all planets.
        """
        p1, p2, p3 = self._get_planet_cartesians()
        return Rect(p1, p2).contain(p3)

    is_opt_season = has_planetary_alignment

    def is_wet_season(self):
        """
        :return: true if a wet season. This occurs when the sun is in triangle formed by the position of
                    other system's celestial bodies
        """
        sun_coords = self._sun.coor.to_cartesian()
        return sun_coords.is_in_triangle(*self._get_planet_cartesians())

    def get_planets_triangle_perimeter(self):
        """
        :return: the perimeter of triangle formed by system's planet.
        """
        p1, p2, p3 = self._get_planet_cartesians()
        return p1.distance(p2) + p2.distance(p3) + p3.distance(p1)



