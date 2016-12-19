from google.appengine.api import taskqueue

from api.base_handler import BaseRequestHandler
from dao.day_weather_dao import DayWeatherDao

AGE_DAYS = 365
AGES = 10
PREDICTION_PERIOD = AGE_DAYS * AGES


class RunJobHandler(BaseRequestHandler):

    dao = DayWeatherDao()

    def get(self):
        # run job
        taskqueue.add(url='/worker/generate_weather_data', method='POST',
                      queue_name='planetsqueue', params={'days': PREDICTION_PERIOD})

