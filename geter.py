import logging
import traceback
from datetime import date

from input import Input
from api import Api
from common.datatype import Weather



class Geter:
    def __init__(self) -> None:
        self.api = Api()


    def getWeather(self):
        def isDataOk(data):
            if data['status'] != 0:
                logging.error(
                    f"getData for {url} call {data['status']}, reason:{data['message']}")
                logging.error(traceback.format_exc())
                raise Exception

        url = f"https://api.map.baidu.com/weather/v1/?district_id={Input.baidu_district_id}&data_type=all&ak=FOtjhQhTCS8OQN3TitHWGTcjIZziN4XC"
        data = self.api.getData(url)
        isDataOk(data)
        weather = Weather(now_temporature=data['result']['now']['feels_like'],
            low_temporature=data['result']['forecasts'][0]['low'],
            high_temporature=data['result']['forecasts'][0]['high'],
            weather_day=data['result']['forecasts'][0]['text_day'],
            weather_night=data['result']['forecasts'][0]['text_night'])
        return weather

    def getDate(self):
        today = date.today()
        return today



if __name__ == '__main__':
    Geter().getWeather()


