import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tesseract_core
import interface_settings
import test1

def main():



    window_upload_stage = tk.Tk()

    interface_settings.create_window(window_upload_stage)


    #adding text instruction on a window_upload_stage
    text_upload_photo=tk.Label(window_upload_stage, text="CHOOSE PHOTO", font=("Gabriola", 30))
    text_upload_photo.config(anchor=tk.CENTER)
    text_upload_photo.pack()


    f_path = ''
    def browse_a_file():
        f_path=tk.filedialog.askopenfilename(initialdir="/", title="Select an Image", filetype=(("JPG File", "*.jpg"), ("All files", "*.*")))
        if not f_path:
            tk.messagebox.showerror("No Image chosen!", "Please, choose the image.")
            exit()
        else:
            someFunc(f_path)



    

    add_img=tk.PhotoImage(file=r"D:\Python Projects\OCR_Project\plus.png")

    btn_upload=tk.Button(window_upload_stage, text="Add Image", command=browse_a_file)
    btn_upload.config(anchor=tk.CENTER)
    btn_upload.pack()
    def someFunc(f_path):
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
                        text="Save", width =5, height = 5) #callback = SOME_FUNC_TO_SAVE_FILE_MB_WINDOW_TO_CHOOSE_EXTENSION
        button1 = tk.Button(window_output_text,
                        text="Repeat", width =5, height = 5, command=restart) #callback = START_PROGRAM_AGAIN
        button.place(x=200, y=50)
        button1.place(x=300, y=50)






main()
tk.mainloop()

# на те ж вікно додати кнопку збереження тексту і кнопку спробувати ще раз (хз чи точно)
# додати на вибір куди зберегти текст (ворд, тхт,...)


# передбачити помилки (трай кеч + меседжбокси) 
# --- вибраний файл неправильного формату
# 
# зробити .exe
# гарно і логічно розкидати все по файлах
# додати змістовні коментарі
