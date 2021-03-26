import tkinter as tk
import tkinter.ttk as ttk

FONT = ("Verdana",12)

# Based off of my own application in Tkinter previously
class bakerClient(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.wm_title(self, "BakerAI")
        self.geometry("700x500")

        # Container is parent frame, containing all frames
        parent = tk.Frame(self)
        parent.pack(side="top",fill="both",expand=True)
        # Format: min size, weight is z index
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        
        mainFrame = tk.Frame(parent)
        mainFrame.pack(side="top",fill="both",expand=True)
        for i in range(7):
            mainFrame.grid_rowconfigure(index=i, weight=1)
            mainFrame.grid_columnconfigure(index=i, weight=1)


        title = tk.Label(mainFrame, text="Welcome to Sakura's very own BakerAI!", font=FONT)
        title.grid(row=0,column=0,columnspan=7)
        # What we will change to show output
        self.outputLabel = tk.Label(mainFrame, text="Where Bot will Reply", font=FONT)
        self.outputLabel.grid(row=3, column=0, columnspan=2, sticky="NSEW")
        # Input related items
        self.userInput = tk.Entry(mainFrame)
        self.userInput.grid(row=5, column=1, columnspan=4, sticky="EW")
        sendButton = tk.Button(mainFrame, text="Send message", command=lambda: self.getResponse())
        sendButton.grid(row=5, column=6, columnspan=2, sticky="EW")

    def getResponse(self):
        # Get user message
        userMessage = self.userInput.get()
        # Clear the user input
        self.userInput.delete(0, "end")


if __name__ == '__main__':
    client = bakerClient()
    client.mainloop()

