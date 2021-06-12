import nltk
from nltk.corpus import stopwords

from debug import Debug

class Utils:
    stop_words = set(stopwords.words('english'))

    @staticmethod
    def new_line():
        print()

    @staticmethod
    def traverse_nltk_tree(user_input):
        cont = []
        current = []
        for i in user_input:
            
            if type(i) == nltk.Tree:
                current.append(" ".join([token for token, pos in i.leaves()]))
            if current:
                entity = " ".join(current)
                if entity not in cont:
                    cont.append(entity)
                    current = []
            else:
                continue
            return cont

    @staticmethod
    def return_proper_noun(user_input):
        tagged_input = nltk.pos_tag(user_input)
        named_entity_chunked = nltk.ne_chunk(tagged_input, binary=True)
        proper_noun = Utils.traverse_nltk_tree(named_entity_chunked)
        return proper_noun[0]

