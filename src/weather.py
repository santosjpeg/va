import requests

from utils import Utils
from debug import Debug
from _vars import OPENWEATHER_KEY

class Weather:
    @classmethod
    def current_weather(cls, input):
        location = Utils.return_proper_noun(input) 

        Debug.info("Searching the weather in {}...".format(location))
        response = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}".format(location, OPENWEATHER_KEY,"imperial"))
        Debug.debug("Status of API request {}".format(response.status_code)) 

        response_json = response.json()
        weather_levels = response_json["main"]
        weather_desc = response_json["weather"][0]

        temperature = weather_levels["temp"]
        description = weather_desc["description"]

        print("In {}, there is {} with a temperature of {}° F.".format(location,description, temperature))
