import nltk
from nltk.corpus import wordnet

class Define:
    @staticmethod
    def look_up(user_input):
        syns = wordnet.synsets(user_input)
        definition = syns[0].definition()

        try:
            print("The definition of {}: {}".format(user_input, definition))
        except IndexError:
            print("NO WORD FOUND")
