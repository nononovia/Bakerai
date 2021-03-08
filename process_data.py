import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tflearn
import json
import tensorflow
import random

# Load json
with open("intents.json") as jsonFile:
    data = json.load(jsonFile)

allWords = []
convoLabels = []
docs = []

for intent in data["intents"]: # For each "type" of conversation
    if intent["tag"] not in convoLabels:
            convoLabels.append(intent["tag"])
    for pattern in intent["patterns"]: # for each input pattern
        # Stemming: take each word, get "root" word to make learning more accurate

        # To start, get the words with nltk magic
        tempWrds = nltk.word_tokenize(pattern)
        allWords.extend(tempWrds) # Append all words at once
        docs.append(pattern)
        