import webapp2
from google.appengine.api import taskqueue

from api.weather_handler import WeatherHandler


AGE_DAYS = 365
AGES = 10
PREDICTION_PERIOD = AGE_DAYS * AGES


routes = webapp2.WSGIApplication([
    ('/clima', WeatherHandler)
], debug=True)

# run job
taskqueue.add(url='/worker/generate_weather_data', method='POST',
              queue_name='planetsqueue', params={'days': PREDICTION_PERIOD})
