import torch 

import nltk
from nltk.tokenize import word_tokenize

def reply(res):
    print('filler')

def main():
    while(True):
        response = input("Enter: ")
        if response == 'bye':
            break
        else:
            reply(response)

if __name__ == '__main__':
    main()
