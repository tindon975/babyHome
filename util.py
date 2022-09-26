from datetime import date
from common.datatype import Weather, WeatherSuggest, DateSuggest

class Util:
    def __init__(self) -> None:
        pass

    def getWeatherSuggest(self, weather: Weather):
        weatherSuggest = WeatherSuggest(weather)
        return weatherSuggest

    def getDateSuggest(self, today: date):
        week = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        week = week[today.weekday()]

        birthday = date(2000, 9, 17)
        if birthday < today:
            birthday = birthday.replace(year = today.year + 1)
        birthdayCountdown = (birthday - today).days
        
        anniversaryOfLove = date(2021, 3, 3)
        anniversaryOfLovePass = (today - anniversaryOfLove).days + 1
        
        exam = date(2022, 12, 24)
        examPass = (exam - today).days

        dateSuggest = DateSuggest(today, week, birthdayCountdown, anniversaryOfLovePass, examPass)

        return dateSuggest



if __name__ == '__main__':
    Util().getDateSuggest()