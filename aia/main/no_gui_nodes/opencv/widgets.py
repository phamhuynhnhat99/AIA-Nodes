import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class ReadImageWidget():

    def __init__(self):
        self.image_path = 'aia.png'

    def get_image_path(self):
        
        def select_file():
            filetypes = (
                ('png files', '*.png'),
                ('jpg files', '*.jpg'),
                ('All files', '*.*')
            )

            filename = filedialog.askopenfilename(
                title='Open a file',
                initialdir='/',
                filetypes=filetypes)
            if filename:
                print(filename)
                self.image_path = filename
            root.quit()
        
        root = tk.Tk()
        root.title('CHOOSE AN IMAGE')
        root.resizable(False, False)
        root.geometry('200x100')

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