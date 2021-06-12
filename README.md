# Project VA - An Indie Virtual Assistant
A personal voice assistant using ML and speech recognition technologies.

## Changelog
1.3.3:
* Early build of birthday() function (depended on Wikipedia-API library) completed.

1.3.2:
* Removed part of speech/named entity recognition and RegEx chunking during initial cleaning of user response.
* Programmed simple `Question.look_up()` function using `wordnet` corpus as database for definitions of known 

1.3.1:
* Initializing `debug.py` and `utils.py` as practical modules in developmental use.
* Use RegEx parsing utility in NLTK for higher-level NLP speech chunking.

1.2.0:
* Used NLTK's stopwords to clean user responses (reduces number of tokens).
* Implement part of speech (POS) tagging.

1.1.0:
* Initial build!
* Setup server and virtual assistant components
* Takes in user input and tokenizes them by word and punctuation.

**NOTE:** Once long enough, this would be migrated to a CHANGELOG.md document.

## Caveats
* As of right now, speech recognition has not been implemented just yet. So, it is currently a *chatbot* with 
web scraping capabilities.
* This is in very EARLY EARLY ALPHA build, so by no means is the codebase robust.
* The most early versions of the requirements.txt document will be a copy and paste of `pip3 list`, as I open
up more free time I can get rid of unnecessary libraries.

## Dependencies
* NLTK
* SpeechRecognition
* Wikipedia-API <br />

**Disclaimer:** Every single required library used for my personal development is contained in the
`requirements.txt` file.

## Development
Requirement: python3 and pip3 installed alongside capability of making python virtual environments. <br />

1. Clone or fork this repo and `cd` into the directory
2. `mkdir env` and `cd` into it 
3. Create virtual environment using this command: `python -m venv va` 
4. Install all dependencies with `pip3 install -r ../requirements.txt` 
5. `cd src/` to start developing!
