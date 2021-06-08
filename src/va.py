import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from debug import Debug

class va:
    stop_words = set(stopwords.words('english'))
    debugger = Debug()

    def process(self, raw_response):
        tokens = word_tokenize(raw_response)

        cleaned = []
        for token in tokens:
            if token not in self.stop_words:
                cleaned.append(token)

        cleaned_tagged = nltk.pos_tag(cleaned)
        self.debugger.info("CLEANED + TAGGED: {}".format(cleaned_tagged))
        
        chunk_gram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
        chunk_parser = nltk.RegexpParser(chunk_gram)
        chunked = chunk_parser.parse(cleaned_tagged)

        for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
            self.debugger.info(subtree)
        
        return cleaned_tagged

    def respond(self, cleaned_response):
        pass
