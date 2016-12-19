import webapp2
from webapp2 import Route

from api.run_job_handler import RunJobHandler
from api.weather_handler import WeatherHandler

routes = webapp2.WSGIApplication([

    Route(r'/api/clima', WeatherHandler),
    Route(r'/api/run_job', RunJobHandler)

], debug=True)
