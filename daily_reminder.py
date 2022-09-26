from unicodedata import name
from geter import Geter
from util import Util
from pusher import Pusher


class DailyReminder:
    def __init__(self) -> None:
        self.geter = Geter()
        self.util = Util()
        self.pusher = Pusher()

    def goodMorning(self):
        weather = self.geter.getWeather()
        date = self.geter.getDate()
        
        weatherSuggest = self.util.getWeatherSuggest(weather)
        dateSuggest = self.util.getDateSuggest(date)
        
        self.pusher.pushMessage(weatherSuggest, dateSuggest)

if __name__ == "__main__":
    DailyReminder().goodMorning()
