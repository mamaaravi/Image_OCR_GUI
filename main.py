import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tesseract_core
import tk_setup

def start_tesseract():
    '''Browsing a file, running tesseract'''
    global f_path
    f_path=''

    while True:
        f_path=tk.filedialog.askopenfilename(initialdir="/", title="Select an Image", 
                            filetype=(("PNG file", "*.png"), ("JPG file", "*.jpg"), ("JPEG file", "*.jpeg"), ("All files", "*.*")))
        if not f_path:
            msg=tk.messagebox.askquestion("Warning!", "No Image chosen! Would you like to try again?")
            if msg=="yes":
                pass
            else:
                exit()

        else:
            try:
                window_upload_stage.withdraw()
                tesseract_core.image_ocr(f_path)
                tk_setup.save_window(file_save, restart)
                break
            except OSError:
                tk.messagebox.showerror("Error!", "Bad file extension. PNG, JPG, JPEG required.")
            except tk.TclError:
                tk.messagebox.showerror("Error!", "System error! Exiting the application.")

                exit()


def file_save():
    if tk_setup.var.get() == 0:
        extension = '.pdf'
    elif tk_setup.var.get() == 1:
        extension = '.doc'
    elif tk_setup.var.get() == 2:
        extension = '.txt'
    try:
        fout = tk.filedialog.asksaveasfile(mode='w', defaultextension=extension)
        fout.write(tesseract_core.str_tess)
        fout.close()
        tk.messagebox.showinfo("Img OCR", "Successfully saved!")
    except AttributeError:
        tk.messagebox.showerror("No path chosen!", "Please, choose the path.")

def restart():
    tk_setup.window_output_text.destroy()
    main()


def main():
    global window_upload_stage
    window_upload_stage = tk.Tk()
    tk_setup.create_window(window_upload_stage)
    
    global add_img
    add_img=tk.PhotoImage(file=r"D:\Python Projects\OCR_Project\plus.png")


    text_upload_photo=tk.Label(window_upload_stage, text="CHOOSE PHOTO", font=("Gabriola", 30))
    text_upload_photo.config(anchor=tk.CENTER)
    text_upload_photo.pack()

    try:
        btn_upload=tk.Button(window_upload_stage, image=add_img, command=start_tesseract)
    except tk.TclError:
        btn_upload=tk.Button(window_upload_stage, text="Add Image", command=start_tesseract)
    btn_upload.config(anchor=tk.CENTER)
    btn_upload.pack()
    



main()
tk.mainloop()

