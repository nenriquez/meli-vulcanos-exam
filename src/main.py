from model.planetary_system import PlanetaryWeather
from model.predictor import Predictor

AGE_DAYS = 365
AGES = 10
PREDICTION_PERIOD = AGE_DAYS * AGES


def main():
    weather_counter_map, day_when_rainy_a_lot = Predictor.predict_weather(PREDICTION_PERIOD)

    print "Days of DROUGHT {}".format(weather_counter_map[PlanetaryWeather.DROUGHT_SEASON])
    print "Days of WET {}".format(weather_counter_map[PlanetaryWeather.WET_SEASON])
    print "Day when rainy a lot was the number {}".format(day_when_rainy_a_lot)
    print "Days of OTP {}".format(weather_counter_map[PlanetaryWeather.OTP_SEASON])


if __name__ == "__main__": main()