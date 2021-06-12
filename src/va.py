"""
To-do List:
    - Utilize weather and geolocation APIs to develop weather function(s)
Changelog:
    -- 1.3.2
        Took away chunking and implemented simple look_up() function to find definitions of words
    -- 1.3.1
        Created debugging and drawing utilities + RegEx parsing for chunking user responses.
    -- 1.2.0
        Cleans user input with stop words and part of speech (POS) tagging.
    -- 1.1.0
        Initially released with only word tokenization.
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
                Questions.birthday(cleaned)
            elif "who" in cleaned or "Who" in cleaned:
                Questions.who(cleaned)
            elif "weather" in cleaned:
                Questions.current_forecast(cleaned)
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
