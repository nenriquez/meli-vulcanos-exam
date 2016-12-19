import logging

from google.appengine.ext import ndb

from model.day_weather import DayWeather


class DataStoreDayWeather(ndb.Model):

    day = ndb.IntegerProperty()
    weather = ndb.IntegerProperty()


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
            entity.put()

        logging.info("saving entities")

        # TODO: revisar pq esto dejor de crear entidades
        # ndb.put_multi(to_save)

    def get_by_day(self, day):
        result = DataStoreDayWeather.query(DataStoreDayWeather.day == day)
        return DayWeather(result.day, result.weather) if result else None