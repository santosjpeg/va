import nltk

class People:
    @staticmethod
    def birthday(user_input):
        ne_chunked = nltk.ne_chunk(user_input, binary=True)
        print(ne_chunked)
        person_name = [ i for i in ne_chunked.subtrees(filter=lambda t: t.label() == "NE")][0]
        print(person_name)
        print(type(person_name))

            
