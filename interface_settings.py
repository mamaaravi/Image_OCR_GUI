import tkinter as tk 
import tkinter.filedialog
import tkinter.messagebox
import tesseract_core
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

def messageboxes():
    pass



