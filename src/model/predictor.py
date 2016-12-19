from model.day_weather import DayWeather
from model.planetary_system import PlanetaryWeather, PlanetarySystem


class Predictor:

    def __init__(self):
        pass

    @staticmethod
    def predict_weather(days):
        weather_counter_map = {
            PlanetaryWeather.WET_SEASON: 0,
            PlanetaryWeather.NORMAL_SEASON: 0,
            PlanetaryWeather.OTP_SEASON: 0,
            PlanetaryWeather.DROUGHT_SEASON: 0,
        }
        max_perimeter = 0
        day_when_rainy_a_lot = 0

        system = PlanetarySystem()

        for i in range(0, days):
            system.grownup(1)
            weather = system.get_today_weather()
            weather_counter_map[weather] += 1

            if weather == PlanetaryWeather.WET_SEASON:
                perimeter = system.get_planets_triangle_perimeter()
                if perimeter > max_perimeter:
                    max_perimeter = perimeter
                    day_when_rainy_a_lot = i

        return weather_counter_map, day_when_rainy_a_lot

    @staticmethod
    def predict_weather_day(days):
        weather_day_list = []

        system = PlanetarySystem()

        for i in range(0, days):
            system.grownup(1)
            weather = system.get_today_weather()
            weather_day_list.append(DayWeather(i, weather))

        return weather_day_list
