import nltk
from nltk.tokenize import RegexpTokenizer

import wikipediaapi as wiki

from utils import Utils
from debug import Debug

class People:
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    tokenizer = RegexpTokenizer(r'\w+')
    wiki_obj = wiki.Wikipedia(
            language="en",
            )

    @classmethod
    def birthday(cls,user_input):

        ne_tagged = nltk.pos_tag(user_input)
        ne_chunked = nltk.ne_chunk(ne_tagged, binary=True)

        raw_name = [chunk for chunk in ne_chunked.subtrees(filter=lambda t: t.label() == "NE")]

        Debug.info("Raw nltk.tree.Tree data for named entity - {}".format(raw_name))

        person_name = Utils.traverse_nltk_tree(ne_chunked)[0]

        wiki_page = cls.wiki_obj.page(person_name)
        existence = "FOUND" if wiki_page.exists() else "NOT FOUND"
        Debug.info("Looking up {}... {}.".format(person_name, existence))
        
        summary = cls.tokenizer.tokenize(wiki_page.summary[0:100])
        Debug.info(summary)

        birth_month = None
        index_of_month = None
        for i in cls.months:
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

    @classmethod
    def who(cls,user_input):
        ne_tagged = nltk.pos_tag(user_input)
        ne_chunked = nltk.ne_chunk(ne_tagged, binary=True)

        raw_name = [chunk for chunk in ne_chunked.subtrees(filter=lambda t: t.label() == "NE")]

        Debug.info("Raw nltk.tree.Tree data for named entity - {}".format(raw_name))

        person_name = Utils.traverse_nltk_tree(ne_chunked)[0]

        wiki_page = cls.wiki_obj.page(person_name)
        existence = "FOUND" if wiki_page.exists() else "NOT FOUND"
        Debug.info("Looking up {}... {}.".format(person_name, existence))
        
        summary = wiki_page.summary[0:150] 

        print("{}...".format(summary))
        print("For more information. click this link: {}".format(wiki_page.fullurl))
