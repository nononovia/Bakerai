import numpy
import random
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
    print("Hello! This is the chatbot. I am here to make your shopping experience at Sakura effortless! (type 'quit' to quit.) Let's chat:", flush = True)
    while True: 
        reading = input()
        if reading.strip().lower() == "quit": 
            break 
        #get the prediction matrix with the probabilities of correct responses.
        output = model.predict([convert_input_to_bow(reading, allWords )])
        #get the prediction with max probability.
        output_i = numpy.argmax(output)

        #extract the correct response from intents.json.
        cor_label = convoLabels[output_i]
        for label in data['intents']: 
            if label['tag'] == cor_label: 
                cor_responses = label['responses']

        #Just print a random response. 
        print(f'bot: {random.choice(cor_responses)}')

if __name__ == "__main__":
    start()

    
