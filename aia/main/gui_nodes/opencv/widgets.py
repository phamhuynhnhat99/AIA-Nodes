import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class ReadImageWidget():

    def __init__(self):
        self.image_path = ''

    def get_image_path(self):
        
        def select_file():
            filetypes = (
                ('jpg files', '*.jpg'),
                ('png files', '*.png'),
                ('All files', '*.*')
            )

            filename = filedialog.askopenfilename(
                title='Open a file',
                initialdir='/home/',
                filetypes=filetypes)
            if filename:
                r.destroy()
                r.quit()
                self.image_path = filename
        
        r = tk.Tk()
        r.title('CHOOSE AN IMAGE')
        r.resizable(False, False)
        r.geometry('400x300')

        open_button = ttk.Button(
            r,
            text='Open a File',
            command=select_file
        )

        open_button.pack(expand=True)

        r.mainloop()

        return self.image_path


class export_widgets:

    ReadImageWidget = ReadImageWidget
