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

        person_name = Utils.return_proper_noun(user_input)

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

        person_name = Utils.return_proper_noun(user_input)

        wiki_page = cls.wiki_obj.page(person_name)
        existence = "FOUND" if wiki_page.exists() else "NOT FOUND"
        Debug.info("Looking up {}... {}.".format(person_name, existence))
        
        summary = wiki_page.summary[0:150] 

        print("{}...".format(summary))
        print("For more information. click this link: {}".format(wiki_page.fullurl))

    @staticmethod 
    def user_birthday():
        print("Happy birthday!")
