from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from debug import debugger
from responses import Responses

class va:
    stopWords = set(stopwords.words('english'))

    def parse(self, res):
        words = word_tokenize(res)
        return words
    
    def clean(self, lines):
        clean = [] 

        for i in lines:
            if i not in self.stopWords:
                clean.append(i)
        return clean

    def reply(self, res):
        lines = self.parse(res)
        finalLines = self.clean(lines)
        debugger.info(finalLines) 

        for i in lines:
            Responses.process(i)
            
