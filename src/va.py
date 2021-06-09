"""
To-do List:
    - lorem

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

        cleaned_tagged = nltk.pos_tag(cleaned)
        
        return cleaned_tagged

    def respond(self, cleaned):
        self.debugger.info(cleaned)
        words = []
        for i in range(len(cleaned)):
            pos_pair = cleaned[i]
            words.append(pos_pair[0])

        if "define" in words: 
            word_of_interest = words[-1]
            Function.look_up(word_of_interest)
        elif "birthday" in words:
            Function.birthday(cleaned)
        
