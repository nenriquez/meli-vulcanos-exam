from google.appengine.ext import ndb

from model.day_weather import DayWeather


class DataStoreDayWeather(ndb.Model):

    day = ndb.IntegerProperty()
    weather = ndb.StringProperty()


class DayWeatherDao:

    def save(self, day_weather_model):
        day_weather = DayWeatherDao()
        day_weather.day = day_weather_model.day
        day_weather.weather = day_weather_model.weather
        day_weather.put()

    def save_all(self, list):
        to_save = []

        for d in list:
            entity = DataStoreDayWeather()
            entity.day = d.day
            entity.weather = d.weather

        ndb.put_multi(to_save)

    def get_by_day(self, day):
        result = DayWeatherDao.query(DayWeatherDao.day == day)
        return DayWeather(result.day, result.weather) if result else None