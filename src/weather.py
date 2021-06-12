import nltk
import requests
from requests.auth import HTTPBasicAuth
import json

from utils import Utils
from debug import Debug

#CONFIDENTIAL
from vars import WEATHERAPI_KEY, WEATHERAPI_URL

class Weather:
    @classmethod
    def current_forecast(cls, input):
        headers = {'Authorization': 'Bearer {}'.format(WEATHERAPI_KEY)}
        Debug.info(headers)
        response = requests.get(WEATHERAPI_URL, headers=headers)
        Debug.info("Requesting... CODE {}".format(response.status_code))
        
