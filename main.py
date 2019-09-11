import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tesseract_core
import interface_settings
var = 0

def file_save():
    global var
    if var.get() == 0:
        extension = '.pdf'
    elif var.get() == 1:
        extension = '.doc'
    elif var.get() == 2:
        extension = '.txt'
    try:
        fout = tk.filedialog.asksaveasfile(mode='w', defaultextension=extension)
        fout.write(tesseract_core.str_tess)
        fout.close()
        tk.messagebox.showinfo("Img OCR", "Successfully saved!")
    except AttributeError:
        tk.messagebox.showerror("No path chosen!", "Please, choose the path.")





def main():

    window_upload_stage = tk.Tk()

    interface_settings.create_window(window_upload_stage)
    global add_img
    add_img=tk.PhotoImage(file=r"D:\Python Projects\OCR_Project\plus.png")


    #adding text instruction on a window_upload_stage
    text_upload_photo=tk.Label(window_upload_stage, text="CHOOSE PHOTO", font=("Gabriola", 30))
    text_upload_photo.config(anchor=tk.CENTER)
    text_upload_photo.pack()


    f_path = ''
    def browse_a_file():
        f_path=tk.filedialog.askopenfilename(initialdir="/", title="Select an Image", filetype=(("PNG File", "*.png"), ("All files", "*.*")))
        # if not f_path:
        #     tk.messagebox.showerror("No Image chosen!", "Please, choose the image.")
        # else:
        #     someFunc(f_path)
        try:
            f_path=tk.filedialog.askopenfilename(initialdir="/", title="Select an Image", filetype=(("PNG File", "*.png"), ("All files", "*.*")))
        except AttributeError:
            tk.messagebox.showerror("No Image chosen!", "Please, choose the image.")
            exit()
           



    


    btn_upload=tk.Button(window_upload_stage, image=add_img, command=browse_a_file)
    btn_upload.config(anchor=tk.CENTER)
    btn_upload.pack()

    
    def someFunc(f_path):
        global var
        window_upload_stage.destroy()
        tesseract_core.image_ocr(f_path)
        window_output_text = tk.Tk()
        def restart():
            window_output_text.destroy()
            main()
        interface_settings.create_window(window_output_text)
        text_ocr = tk.Text(window_output_text, height=100, width=300, borderwidth=0)
        text_ocr.insert(1.0,  tesseract_core.str_tess)  
        text_ocr.place(x=0, y=250)
        text_ocr.configure(state="disabled")
        text_ocr.configure(inactiveselectbackground=text_ocr.cget("selectbackground"))

        button = tk.Button(window_output_text,
                        text="Save", width =5, height = 5, command=file_save)
        button1 = tk.Button(window_output_text,
                        text="Repeat", width =5, height = 5, command=restart) 
        button.place(x=200, y=50)
        button1.place(x=300, y=50)
        var = tk.IntVar()
        var.set(0)
        radiobutton1 = tk.Radiobutton(window_output_text, text  = 'PDF',  variable=var, value=0)
        radiobutton2 = tk.Radiobutton(window_output_text, text='DOC', variable=var, value=1)
        radiobutton3 = tk.Radiobutton(window_output_text, text='TXT', variable=var, value=2)
        radiobutton1.place(x=500, y=50)
        radiobutton2.place(x=500,y=70)
        radiobutton3.place(x=500,y=90)




main()
tk.mainloop()



# зробити .exe
# гарно і логічно розкидати все по файлах
# додати змістовні коментарі
