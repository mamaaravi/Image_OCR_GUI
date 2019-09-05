import tkinter as tk 
import tkinter.filedialog
import tkinter.messagebox
import threading
import tesseract_core
import interface_settings

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
    else:
        func(f_path)





add_img=tk.PhotoImage(file=r"D:\Python Projects\OCR_Project\plus.png")
btn_upload=tk.Button(window_upload_stage, image=add_img, command=browse_a_file)
btn_upload.config(anchor=tk.CENTER)
btn_upload.pack()
def func(f_path):
    window_upload_stage.destroy()

    thread_progressbar=threading.Thread(target=interface_settings.progress_bar)
    thread_img_ocr=threading.Thread(target=tesseract_core.image_ocr, args=(f_path,))

    thread_progressbar.start() 
    thread_img_ocr.start()
    thread_progressbar.join()
    thread_img_ocr.join()

    if not thread_img_ocr.is_alive():
        window_output_text=tk.Tk()
        interface_settings.create_window(window_output_text)
        # text_ocr=tk.Label(window_output_text, text=tesseract_core.str_tess, font=("Arial", 16 ))
        # text_ocr.config(anchor=tk.CENTER)
        # text_ocr.pack()
        text_ocr = tk.Text(window_output_text, height=100, borderwidth=0)
        text_ocr.insert(1.0, tesseract_core.str_tess)
        text_ocr.pack()
        text_ocr.configure(state="disabled")
        text_ocr.configure(inactiveselectbackground=text_ocr.cget("selectbackground"))

window_save_text=tk.Tk()
interface_settings.create_window(window_save_text)


window_upload_stage.mainloop()



# виправити вивід тексту на екран: щоб він не виводився поза межі вікна
# на те ж вікно додати кнопку збереження тексту і кнопку спробувати ще раз (хз чи точно)
# додати на вибір куди зберегти текст (ворд, тхт,...)

# придумати красивий інтерфейс
# реалізувати красивий інтерфейс
# передбачити помилки (трай кеч + меседжбокси) 
# --- вибраний файл неправильного формату
# 
# зробити .exe
# гарно і логічно розкидати все по файлах
# додати змістовні коментарі
