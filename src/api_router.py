import webapp2

from api.run_job_handler import RunJobHandler
from api.weather_handler import WeatherHandler

routes = webapp2.WSGIApplication([
    ('/clima', WeatherHandler)
    ('/run_job', RunJobHandler)
], debug=True)
