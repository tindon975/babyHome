import logging
import traceback
import json
from api import Api
from common.datatype import DateSuggest, WeatherSuggest

class Pusher:
    def __init__(self) -> None:
        self.api = Api()



    def pushMessage(self, weatherSuggest, dateSuggest):
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

        def getAccessToken():
            def isDataError(data):
                if data['errcode'] != 0:
                    logging.error(
                        f"getData for {url} call {data['errcode']}, reason:{data['errmsg']}")
                    logging.error(traceback.format_exc())
                    raise Exception

            url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwdedfaa514c89fd9e&corpsecret=Rk7Ub9Ap18szQ5TRi9b7mqf4HZdCF_e7Qm1Lcj3pxE0"
            data = self.api.getData(url)
            isDataError(data)
            accessToken = data['access_token']
            return accessToken

        def isDataError(data):
            if data['errcode'] != 0:
                logging.error(
                    f"getData for {url} call {data['errcode']}, reason:{data['errmsg']}")
                logging.error(traceback.format_exc())
                raise Exception

        message = getMessage(weatherSuggest, dateSuggest)
        message = json.dumps(message)
        accessToken = getAccessToken()
        url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={accessToken}"

        data = self.api.postData(url, message)
        isDataError(data)
        
            

    


    
        
    

