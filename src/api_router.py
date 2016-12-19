import webapp2
from webapp2 import Route

from api.run_job_handler import RunJobHandler
from api.weather_handler import WeatherHandler

routes = webapp2.WSGIApplication([
    Route('r/clima', WeatherHandler),
    Route('r/run_job', RunJobHandler)
], debug=True)
