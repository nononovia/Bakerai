import numpy
import random
import pickle
import sklearn
from process_data import  allWords, convoLabels, data
from NN import convert_input_to_bow
from NN import model
# these are the model and function for chatting
# from process_data import ..... (you can load functions, varibles....)

#Write a message introducing the chatbot, and print the message to the console
#Write a loop to repeatedly prompt the user for input, and store that input in a variable. (variable as a function input later)
#terminate the loop after the user inputs a reserved value of your choosing


#start chat - 'quit' to quit.

def start():
    print("\n\n\n\n\n")
    print("Hello! This is the chatbot. I am here to tell you about the bakery Sakura! (type 'quit' to quit.) Let's chat:", flush = True)
    loaded_clf = load_sentiment_analysis()[0]
    while True:
        reading = input()
        if reading.strip().lower() == "quit":
            break
        #get the prediction matrix with the probabilities of correct responses.
        output = model.predict([convert_input_to_bow(reading, allWords )])
        #get the prediction with max probability.


        #get the sentiment of user input
        sent_out = loaded_clf.predict(input_to_bow_sentiment(reading))
        print(sent_out)

        # #extract the correct response from intents.json.
        # cor_label = convoLabels[output_i]
        # for label in data['intents']:
        #     if label['tag'] == cor_label:
        #         cor_responses = label['responses']

        #Just print a random response.
        print(f'bot: {random.choice(output_depending_on_sentiment(sent_out,output))}')
        print(" ")





def load_sentiment_analysis(): 
    with open('./sentiment_models/sentiment_model.pkl', 'rb') as f:
        loaded_clf = pickle.load(f)

    with open('./sentiment_models/vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    return [loaded_clf,vectorizer]

def input_to_bow_sentiment(words): 
    vectorizer = load_sentiment_analysis()[1]
    wrds_list = [words]
    wrds_list_bow = vectorizer.transform(wrds_list)
    return wrds_list_bow

def output_depending_on_sentiment(sentiment,output):
    if sentiment == "NEGATIVE":
        cor_label = "negative"
    else:
        if numpy.amax(output) > 0.5:
            output_i = numpy.argmax(output)
            cor_label = convoLabels[output_i]
        else:
            cor_label = "default";
        # extract the correct response from intents.json.
    for label in data['intents']:
        if label['tag'] == cor_label:
            cor_responses = label['responses']
    return cor_responses



       

if __name__ == "__main__":
    start()
