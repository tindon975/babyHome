import logging
import traceback
import json
from api import Api
from common.datatype import DateSuggest, WeatherSuggest

class Pusher:
    def __init__(self) -> None:
        self.api = Api()



    def pushMessage(self, message):
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

        accessToken = getAccessToken()
        url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={accessToken}"

        data = self.api.postData(url, message)
        isDataError(data)
        
            

    


    
        
    

