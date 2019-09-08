import tkinter as tk 
import interface_settings
import tesseract_core

def save_txt():
    f= open("OCR_text.txt","w+", encoding="utf-8")
    f.write(tesseract_core.str_tess)
    f.close()
def save_doc():
    f= open("OCR_text.doc","w+", encoding="utf-8")
    f.write(tesseract_core.str_tess)
    f.close()
def save_pdf():
    f= open("OCR_text.pdf","w+", encoding="utf-8")
    f.write(tesseract_core.str_tess)
    f.close()

