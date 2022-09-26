import json
from common.datatype import DateSuggest, WeatherSuggest
from geter import Geter
from util import Util
from pusher import Pusher


class DailyReminder:
    def __init__(self) -> None:
        self.geter = Geter()
        self.util = Util()
        self.pusher = Pusher()

    def goodMorning(self):
        def getMessage(weatherSuggest: WeatherSuggest, dateSuggest: DateSuggest):
            message = {
                'touser': "LiaoZuoYou",
                'msgtype': "news",
                'agentid': 1000002,
                'news': {
                    'articles':
                    [
                        {
                        'title': "晚上好呀大宝贝！",
                        'description': f"今天是{dateSuggest.today.month}月{dateSuggest.today.day}日 {dateSuggest.week}\n"
                            + f"当前气温{weatherSuggest.weather.now_temporature}, 今日最高气温{weatherSuggest.weather.high_temporature}, 最低气温{weatherSuggest.weather.low_temporature}\n"
                            + f"今天白天天气{weatherSuggest.weather.weather_day}, 晚上天气{weatherSuggest.weather.weather_night}\n"
                            + f"今天是我们恋爱的{dateSuggest.anniversary_of_love_pass}天\n"
                            + f"距离宝贝生日还有{dateSuggest.birthday_countdown}天呢\n"
                            + f"还有{dateSuggest.exam_countdown}天就要上战场啦",
                        "picurl": 'http://42.192.223.150:4000/cute.jpg'
                        }
                    ]
                }
            }
            return message

        weather = self.geter.getWeather()
        date = self.geter.getDate()
        
        weatherSuggest = self.util.getWeatherSuggest(weather)
        dateSuggest = self.util.getDateSuggest(date)

        message = getMessage(weatherSuggest, dateSuggest)
        message = json.dumps(message)
        
        self.pusher.pushMessage(message)

if __name__ == "__main__":
    DailyReminder().goodMorning()
