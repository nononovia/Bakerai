#Write a message introducing the chatbot, and print the message to the console
print("Hello! This is the chatbot. I am here to boost your mental wellbeing! Let's chat:", flush = True)
#Write a loop to repeatedly prompt the user for input, and store that input in a variable. (variable as a function input later)
#terminate the loop after the user inputs a reserved value of your choosing
END_CONVO = "0"

if __name__ == "__main__"
    i = True
    while i == True:
        reading = input()
        if reading == END_CONVO:
            i = False
        else: # Send response to user
            print("E\n")

