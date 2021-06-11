import nltk
from nltk.tokenize import RegexpTokenizer

import wikipediaapi as wiki

from utils import Utils
from debug import Debug

class People:
    @staticmethod
    def birthday(user_input):
        months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        tokenizer = RegexpTokenizer(r'\w+')
        wiki_obj = wiki.Wikipedia(
                language="en",
                )

        ne_chunked = nltk.ne_chunk(user_input, binary=True)

        raw_name = [chunk for chunk in ne_chunked.subtrees(filter=lambda t: t.label() == "NE")]

        Debug.info("Raw nltk.tree.Tree data for named entity - {}".format(raw_name))

        person_name = Utils.traverse_nltk_tree(ne_chunked)[0]

        wiki_page = wiki_obj.page(person_name)
        existence = "FOUND" if wiki_page.exists() else "NOT FOUND"
        Debug.info("Looking up {}... {}.".format(person_name, existence))
        
        summary = tokenizer.tokenize(wiki_page.summary[0:100])
        Debug.info(summary)

        birth_month = None
        index_of_month = None
        for i in months:
            for j in range(len(summary)):
                if i == summary[j]:
                    birth_month = i
                    index_of_month = j

        Debug.info("BIRTH MONTH FOUND - {}".format(birth_month))

        if person_name[-1] == 's':
            person_name += "'"
        else:
            person_name += "'s"
        print("{} birthday is {} {}, {}".format(person_name, birth_month, summary[index_of_month + 1], summary[index_of_month + 2]))

    @staticmethod
    def who(user_input):
        pass
