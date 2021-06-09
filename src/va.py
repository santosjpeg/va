"""
To-do List:
    - Replace RegEx chunking with Natural Entity Recognition to emphasize proper nouns.
    - Implement chunking in respond() function for more accurate conditionals.

Changelog:
    - 1.3.2: Took away chunking and implemented simple look_up() function to find definitions of words
    - 1.3.1: Created debugging and drawing utilities + RegEx parsing for chunking user responses.
    - 1.2.0: Cleans user input with stop words and part of speech (POS) tagging.
    - 1.1.0: Initially released with only word tokenization.
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from debug import Debug
from function import Function

class va(Function):
    stop_words = set(stopwords.words('english'))
    debugger = Debug()

    def process(self, raw_response):
        tokens = word_tokenize(raw_response)
        cleaned = []
        for token in tokens:
            if token not in self.stop_words:
                cleaned.append(token)
        return cleaned

    def respond(self, cleaned):
        if "define" in cleaned: 
            Function.look_up(cleaned[-1])
        
