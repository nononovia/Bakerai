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
