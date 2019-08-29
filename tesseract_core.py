try:
    from PIL import Image
except ImportError:
    import Image


import pytesseract

'''Including full path to tesseract executable if pytesseract is not in the PATH '''
pytesseract.pytesseract.tesseract_cmd = r'D:\Python Projects\Tesseract-OCR\tesseract.exe'



def image_ocr(image_path):
    '''This function uses pytesseract to recognize text at an image given by user.'''
    global str_tess
    print("start thread img ocr")
    img = Image.open(image_path)
    str_tess=pytesseract.image_to_string(img)
    
    print(str_tess)
    print("finish thread img ocr")
