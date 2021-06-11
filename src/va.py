"""
To-do List:
    - Replace conditional statements in respond() method to comparing RegEx structure

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
        if "define" in cleaned or "Define" in cleaned:
            Questions.look_up(cleaned)
        elif "birthday" in cleaned:
            Questions.birthday(cleaned)
        elif "who" in cleaned or "Who" in cleaned:
            Questions.who(cleaned)
        
