import json

from webapp2 import exc

from api.api_utils import require_params
from api.base_handler import BaseRequestHandler
from dao.day_weather_dao import DayWeatherDao


class WeatherHandler(BaseRequestHandler):

    dao = DayWeatherDao()

    @require_params(['dia'])
    def get(self):
        day = self.request.get('dia')

        day_weather = self.dao.get_by_day(day)

        if not day_weather:
            raise exc.HTTPNotFound(detail="No day found: {}".format(day))

        self.response.out.write(json.dumps({"dia": day_weather.day, "clima": day_weather.weather_string}))