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

def save_text():
    f= open("OCR_text.txt","w+", encoding="utf-8")
    f.write(tesseract_core.str_tess)
    f.close()
def stop_app():
    return False

 
def change():  
   pass
# def save_text_window():
#     # window_save_text=tk.Tk()
#     # create_window(window_save_text)
#     # btn_save=tk.Button(window_save_text, text="Save text", command=save_text)
#     # btn_save.config(anchor=tk.CENTER)
#     # btn_save.pack()

#     # btn_exit=tk.Button(window_save_text, text="Exit", command=stop_app)
#     # btn_exit.config(anchor=tk.CENTER)
#     # btn_exit.pack()
#     root = tk.Tk()
#     create_window(root)
#     var = tk.IntVar()
#     var.set(0)
#     red = tk.Radiobutton(text="Red", variable=var, value=0)
#     green = tk.Radiobutton(text="Green", variable=var, value=1)
#     blue = tk.Radiobutton(text="Blue", variable=var, value=2)
#     button = tk.Button(text="Изменить", command=change)
#     label = tk.Label(width=20, height=10)
#     red.pack()
#     green.pack()
#     blue.pack()
#     button.pack()
#     label.pack()
# # root.mainloop()
