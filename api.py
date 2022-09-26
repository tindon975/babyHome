import traceback
from urllib import response
import requests
import json
import logging

class Api:
    def __init__(self) -> None:
        pass

    def getData(self, url):
        def isResponseError(response):
            if response.status_code != 200:
                logging.error(
                    f"requests get for {url} call {response.status_code}, reason:{response.reason}")
                logging.error(traceback.format_exc())
                raise Exception

        response = requests.get(url)
        isResponseError(response)
        return response.json()

    def postData(self, url, data):
        def isResponseError(response):
            if response.status_code != 200:
                logging.error(
                    f"requests post for {url} call {response.status_code}, reason:{response.reason}")
                logging.error(traceback.format_exc())
                raise Exception

        response = requests.post(url, data=data)
        isResponseError(response)
        return response.json()