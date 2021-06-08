from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

class va:
    def clean(self, raw_response):
        tokens = word_tokenize(raw_response)
        tokens[0].title()

        return tokens

    def respond(self, cleaned_response):
        pass
