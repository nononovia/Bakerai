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
docs_x = []
docs_pattern = []

for intent in data["intents"]: # For each "type" of conversation
    if intent["tag"] not in convoLabels:
            convoLabels.append(intent["tag"])
    for pattern in intent["patterns"]: # for each input pattern
        # Stemming: take each word, get "root" word to make learning more accurate

        # To start, get the words and remove extra with nltk magic
        tempWrds = nltk.word_tokenize(pattern)
        allWords.extend(tempWrds) # Append all words at once
        
        # Store practice inputs and their classifications
        docs.append(pattern)
        docs_pattern.append(intent["tag"])
# Turn all words to lowercase
allWords = [stemmer.stem(w.lower()) for w in allWords]

# Remove all duplicates, and sort words (for easier use)
allWords = sorted(list(set(words)))

convoLabels = convoLabels.sort()

training = []
output = []

out_empty = [0]*len(convoLabels)

# Idea: take each sentence, turn it into a list of word occurances, with a list of all possible words we are looking at
for i, doc in enumerate(docs_x):
    bag = []
    # Simplify words to the root word
    wrds = [stemmer.stem(w) for w in doc] 

    for word in allWords: 
        if word in wrds: # This word is in our sentence
            bag.append(1)
        else:
            bag.append(0)
    output_row = out_empty[:]
    output_row = [labels.index(docs_patter[i])] = 1

    training.append(bag)
    output.append(output_row)
# Turn data to numpy arrays
training = numpy.array(training)
output = np.array(output)