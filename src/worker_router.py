import webapp2

from worker.generate_weather_data_worker import GenerateWeatherDataWorker

routes = webapp2.WSGIApplication([

    webapp2.Route(r'/worker/generate_weather_data', handler=GenerateWeatherDataWorker),

], debug=True)
