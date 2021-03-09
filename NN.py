import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tflearn
import json
import tensorflow
import random
from process_data import training, output

tensorflow.reset_default_graph()