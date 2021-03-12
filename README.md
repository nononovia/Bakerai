# Bakerai

## Bakerai is a chat bot for our online bakery store. Bakerai acts as your online assistant to make the shopping experience effortless.

## Project Structure 

bakerai has the following file structure:   

  ---process_data.py  
  ---NN.py  
  ---main.py   
  ---intents.json  

 We have four files which all have one specific purpose as asked by the requirements. 


 ### `process_data.py` 

This file contains code which helps process our 'intents.json' file into a numpy array where each word's frequency corresponds to a cell in multi-dimensional numpy array. This structure is called bag of words in machine learning. 

### `NN.py` 

This file is where the model is trained. after running process_data.py, run this file next. 
We were smart enough so that the code checks first if there is already a model present within the file structure. If not, only then the code uses Tensorflow to train a new model from the bag of words input provided by process_data.py 


### `main.py` 

This is the file which handles interacting with the model. we have a start function which has a while loop so that the user can query the model repeatedly. In the start function, we use the 'convert_input_to_bow()' function from NN.py which converts user input to the bag of words structure (previously mentioned). Then we use the model imported from NN.py, and use TensorFlow's inbuilt 'predict' function. We feed it the output from 'convert_input_to_bow()' function and it uses the model to give us a reply from the 'bot'. 
We then do some processing and return a random response from intents.json depending on what the model classified the input as. 

### `intents.json` 

This is the data which the model is trained on. The model uses the 'tags' and 'patterns' as input when training. Then the trained model is able to take in some text, compare it with the 'patterns' section of each tag and then try to classify the 'tag' depending on the input. Once we have a 'tag' we just return one of the strings from the 'responses' section of the corresponding tag.  


## Functions
- Customer service and support.
- Provide information about products and services to the customer.

## Implementation

Bakerai uses advanced Natural Langugage Processing Techniques and Machine Learning Models to tailor responses specially to your needs.


## Requirements Definition

The ChatBot Bakerai should be able to answer basic day to day questions about the bakery and should keep customers entertained while they are waiting for their purchases??.
The ChatBot should be setted as an online assistant, to give customer information about the bakery before they come, so they can decide whether or not they want to visit.
AND customers can also order from the chatbot (future implementation) when they are in store.

It should be able to answer questions like:

Where is the bakery?

What is the hours of the bakery?

What baked goods are offered?

What specific items cost?

Potential allergies?

##  Sample Output Ideas.

- greetings
  - hi
  - who are you
  - name
- ask about location
- ask about time
- ask about menu
- ask about allergy
- ask about gluten free
- ask to buy cookie
- ask to buy coffee with cookie
- mention coming up wedding/event and ask about customize cake
- ask to buy a cupcake for taste test haha
- tell me a joke
- Have a good day
### This is the official repository hosting the code which powers Bakerai. Feel free to take a look!

# bye - made with ♥ for COSC 310 [Intro to Software Eng.]
