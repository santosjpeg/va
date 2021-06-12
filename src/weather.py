import nltk
import requests
import json

from utils import Utils
from debug import Debug

#CONFIDENTIAL
from vars import IPSTACK_URL

class Weather:
    @classmethod
    def current_forecast(cls, input):
        wanted_location = Utils.return_proper_noun(input)
        Debug.info("Finding the weather for {}...".format(wanted_location))
