import nltk
from utils import Utils
from debug import Debug

class People:
    @staticmethod
    def birthday(user_input):
        ne_chunked = nltk.ne_chunk(user_input, binary=True)
        person_name = [ i for i in ne_chunked.subtrees(filter=lambda t: t.label() == "NE")][0]
        Debug.info("person_name - {} (has a type of {})".format(person_name, type(person_name)))
