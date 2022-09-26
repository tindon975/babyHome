
from dataclasses import dataclass

from dataclasses import dataclass
from datetime import date

@dataclass
class Weather:
    now_temporature: int
    low_temporature: int
    high_temporature: int
    weather_day: str
    weather_night: str

@dataclass
class WeatherSuggest:
    weather: Weather
    
@dataclass
class DateSuggest:
    today: date
    week: str
    birthday_countdown: int
    anniversary_of_love_pass: int
    exam_countdown: int
