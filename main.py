#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a message introducing the chatbot, and print the message to the console
print("Hello! This is the chatbot. I am here to boost your mental wellbeing! Let's chat:", flush = True)
#Write a loop to repeatedly prompt the user for input, and store that input in a variable. (variable as a function input later)
#terminate the loop after the user inputs a reserved value of your choosing
ill = "stressed"
i = True
while i == True:
    reading = input("One word to describe how you feel today:")
    if reading == ill:
        i = False
    else:
        print("E\n")
    #save that reserved value to a constant outside of the "main" method
global value
value = ill

