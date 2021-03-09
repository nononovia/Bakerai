import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tflearn
import json
import tensorflow
import random
from process_data import training, output


tensorflow.reset_default_graph()


nerual_net = tflearn.input_data(shape=[None, len(training[0])])
# this create input data for the RNN 
nerual_net = tflearn.fully_connected(nerual_net, 8)
# first hidden layer with 8 neruon
nerual_net = tflearn.fully_connected(nerual_net, 8)
# second hidden layer with 8 neruon
nerual_net = tflearn.fully_connected(nerual_net, len(output[0]), activation="softmax")
# output layer and declare activiation function for this NN. In this case is softmax
# the activiation function softmax will give a probaility to all output
nerual_net = tflearn.regression(nerual_net)

model = tflearn.DNN(nerual_net)
# this model untilize DNN(deep neural network) for natural langrage processing

model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
# this is where model is trained
# training and output both pass in
# n_epoch is for how many its going to see the same data, in this case its 1000 time(we expect the more we show the same data, the better it is classifying )
# we pass in 8 batch at a time

model.save("model.tflearn")

