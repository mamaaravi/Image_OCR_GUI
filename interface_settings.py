import tkinter as tk 
import tkinter.filedialog
import tkinter.messagebox

import tkinter as tk 
from tkinter import ttk

def create_window(window):
    window.title("Image OCR")
    window.geometry('600x600')
    # get screen width and height
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - 300    
    y = (hs/2) - 300
    window.geometry('%dx%d+%d+%d' % (600, 600, x, y))

def text():
    pass
def messageboxes():
    pass
    
def progress_bar():
    print("start thread bar")
    maxValue=100
    progressbar=tk.ttk.Progressbar(orient="horizontal",length=300,mode="determinate")
    progressbar.pack(side=tk.TOP)
    currentValue=0
    def progress(currentValue):
        progressbar["value"]=currentValue
    progressbar["value"]=currentValue
    progressbar["maximum"]=maxValue
    divisions=10
    for i in range(divisions):
        currentValue=currentValue+10
        progressbar.after(100, progress(currentValue))
        progressbar.update() # Force an update of the GUI
    print("finish thread bar")
    