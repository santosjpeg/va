import nltk
from nltk.corpus import wordnet
from debug import Debug

class Define:
    @staticmethod
    def look_up(user_input):
        word_of_interest = user_input[-2]
        syns = wordnet.synsets(word_of_interest)
        definition = syns[0].definition()

        try:
            print("Definition of {}: {}".format(word_of_interest, definition))
        except IndexError:
            print("NO WORD FOUND")
