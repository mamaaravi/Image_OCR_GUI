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



def save_window(com1, com2):    
    global window_output_text
    window_output_text = tk.Tk()

    create_window(window_output_text)
    text_ocr = tk.Text(window_output_text, height=100, width=300, borderwidth=0)
    text_ocr.insert(1.0,  tesseract_core.str_tess)  
    text_ocr.place(x=0, y=250)
    text_ocr.configure(state="disabled")
    text_ocr.configure(inactiveselectbackground=text_ocr.cget("selectbackground"))
    global var
    var = tk.IntVar()
    var.set(0)
    button = tk.Button(window_output_text,
                    text="Save", width =5, height = 5, command=com1)
    button1 = tk.Button(window_output_text,
                    text="Repeat", width =5, height = 5, command=com2) 
    button.place(x=200, y=50)
    button1.place(x=300, y=50)

    radiobutton1 = tk.Radiobutton(window_output_text, text  = 'PDF',  variable=var, value=0)
    radiobutton2 = tk.Radiobutton(window_output_text, text='DOC', variable=var, value=1)
    radiobutton3 = tk.Radiobutton(window_output_text, text='TXT', variable=var, value=2)
    radiobutton1.place(x=500, y=50)
    radiobutton2.place(x=500,y=70)
    radiobutton3.place(x=500,y=90)  