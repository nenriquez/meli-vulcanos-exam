from model.planetary_system import PlanetaryWeather


class DayWeather:

    _weather_string_map = {
        PlanetaryWeather.NORMAL_SEASON: 'normal',
        PlanetaryWeather.DROUGHT_SEASON: 'sequia',
        PlanetaryWeather.OTP_SEASON: 'condiciones optimas de temperatura y presion',
        PlanetaryWeather.WET_SEASON: 'lluvioso'
    }

    def __init__(self, day, weather):
        self.day = day
        self.weather = weather

    @property
    def weather_string(self):
        return self._weather_string_map.get(self.weather)


