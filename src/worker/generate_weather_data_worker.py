from api.api_utils import require_params, get_int_from_param
from api.base_handler import BaseRequestHandler
from dao.day_weather_dao import DayWeatherDao
from model.predictor import Predictor


class GenerateWeatherDataWorker(BaseRequestHandler):

    @require_params(['days'])
    def post(self):
        days = get_int_from_param(self.request.get('days'))
        weather_day_list = Predictor.predict_weather_day(days)
        DayWeatherDao().save_all(weather_day_list)


