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
                root.destroy()
                root.quit()
                self.image_path = filename
        
        root = tk.Tk()
        root.title('CHOOSE AN IMAGE')
        root.resizable(False, False)
        root.geometry('400x300')

        open_button = ttk.Button(
            root,
            text='Open a File',
            command=select_file
        )

        open_button.pack(expand=True)

        root.mainloop()

        return self.image_path


class export_widgets:

    ReadImageWidget = ReadImageWidget
