import unittest

from exception.exceptions import VirtualMethodException
from model.geometry import Polar
from model.planetary_system import PlanetarySystem, PlanetaryWeather, CelestialBodies


class BasePlanetarySystemTest(unittest.TestCase):

    def setUp(self):
        # conveniet modification of planet position
        self._modify_planet_positon()
        self.system = PlanetarySystem()

    def _modify_planet_positon(self):
        raise VirtualMethodException("_modify_planet_positon")


class PlanetarySystemNormalSeasonTest(BasePlanetarySystemTest):

    def _modify_planet_positon(self):
        CelestialBodies.FERENGI.coor = Polar(500, 45)
        CelestialBodies.BETASOIDE.coor = Polar(2000, 60)
        CelestialBodies.VULCANO.coor = Polar(1000, 75)

    def test_weather(self):
        self.assertEqual(self.system.get_today_weather(), PlanetaryWeather.NORMAL_SEASON)



class PlanetarySystemWetSeasonTest(BasePlanetarySystemTest):

    def _modify_planet_positon(self):
        CelestialBodies.FERENGI.coor = Polar(500, 45)
        CelestialBodies.BETASOIDE.coor = Polar(2000, 270)
        CelestialBodies.VULCANO.coor = Polar(1000, 150)

    def test_weather(self):
        self.assertEqual(self.system.get_today_weather(), PlanetaryWeather.WET_SEASON)


class PlanetarySystemDroughtSeasonTest(BasePlanetarySystemTest):

    def _modify_planet_positon(self):
        CelestialBodies.FERENGI.coor = Polar(500, 45)
        CelestialBodies.BETASOIDE.coor = Polar(2000, 45)
        CelestialBodies.VULCANO.coor = Polar(1000, 225)

    def test_weather(self):
        self.assertEqual(self.system.get_today_weather(), PlanetaryWeather.DROUGHT_SEASON)


class PlanetarySystemOptSeasonTest(BasePlanetarySystemTest):

    def _modify_planet_positon(self):
        CelestialBodies.FERENGI.coor = Polar(500, 45)
        CelestialBodies.BETASOIDE.coor = Polar(1000, 0)
        CelestialBodies.VULCANO.coor = Polar(1000, 90)

    def test_weather(self):
        self.assertEqual(self.system.get_today_weather(), PlanetaryWeather.OTP_SEASON)

