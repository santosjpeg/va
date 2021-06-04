import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

from debug import debugger

class va:
    def process(self, res):
        sentences = sent_tokenize(res)
        for i in range(len(sentences)):
            sentences[i] = word_tokenize(sentences[i])
            debugger.info(sentences[i])
        return sentences

    def reply(self, res):
        x = self.process(res)

