"""
To-Do List:
    - Search for best Weather API to request and scrape information from for weather functionality
    - IMPLEMENT SPEECH RECOGNITION!!!
"""

import nltk
from nltk.tokenize import word_tokenize

from debug import Debug
from questions import Questions
from statements import Statements
from utils import Utils

class va(Questions):

    def process(self, raw_response):
        tokens = word_tokenize(raw_response)
        cleaned = []

        for token in tokens:
            if token not in Utils.stop_words:
                cleaned.append(token)

        return cleaned

    def respond(self, cleaned):
        Debug.info(cleaned)
        if "?" in cleaned:
            Debug.info("This is a question...")
            if "birthday" in cleaned:
                if "my" in cleaned:
                    Statements.user_birthday()
                else:
                    Questions.birthday(cleaned)
            elif "who" in cleaned or "Who" in cleaned:
                Questions.who(cleaned)
            elif "weather" in cleaned:
                Questions.current_weather(cleaned)
            elif "time" in cleaned:
                Questions.tell_time()
            elif "day" in cleaned:
                if "week" not in cleaned:
                    Questions.tell_day()
                else:
                    Questions.tell_day_of_week()
        elif "." in cleaned:
            Debug.info("This is NOT a question...")
            if "define" in cleaned or "Define" in cleaned:
                Statements.look_up(cleaned)
