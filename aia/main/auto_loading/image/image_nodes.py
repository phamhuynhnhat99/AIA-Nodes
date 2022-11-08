from aia.NENV import *

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class ImageNodeBase(Node):

    def __init__(self):
        super().__init__()
        self.image = "None"

    def update_event(self):
        self.image = self.get_image()
        self.set_data_output(key="image", obj=self.image)


class ReadImage(ImageNodeBase):
    title = "Read Image"
    
    def get_image(self):

        self.file_name = ''

        def select_file():
            filetypes = (
                ('jpg files', '*.jpg'),
                ('png files', '*.png'),
                ('All files', '*.*')
            )

            filename = filedialog.askopenfilename(
                title='Open a file',
                initialdir='/home/aia/',
                filetypes=filetypes)
            if filename:
                root.destroy()
                root.quit()
                self.file_name = filename


        if len(self.prev_nodes) == 0:
            self.push_prev_nodes(None)
        else:
            self.set_prev_nodes(ind=0, obj=None)

        root = tk.Tk()
        root.title('CHOOSE AN IMAGE')
        root.resizable(False, False)
        root.geometry('900x600')

        open_button = ttk.Button(
            root,
            text='Open a File',
            command=select_file
        )

        open_button.pack(expand=True)

        root.mainloop()
        
        self.set_fake_input([self.file_name])
        
        img_path = self.get_fake_input()[0]
        image = mpimg.imread(img_path)
            
        return image


class ShowImage(ImageNodeBase):
    title = "Show Image"

    def get_image(self):
        input = self.get_data_inputs(ind=0)
        if input:
            if "image" in input.keys():
                image = input["image"]

                imgplot = plt.imshow(image)
                plt.show()

            else:
                image = "None"
        else:
            image = "None"
        return image


class BlurImage(ImageNodeBase):
    title = "Gaussian Blur Image"

    def get_image(self):

        def a_pixel(a):
            r = 0.0
            g = 0.0
            b = 0.0
            for _ in a:
                r += _[0]
                g += _[1]
                b += _[2]
            r = int(r/len(a))
            g = int(g/len(a))
            b = int(b/len(a))
            return [r, g, b]

        input = self.get_data_inputs(ind=0)
        if input:
            if "image" in input.keys():
                img = input["image"]
                img_w = len(img)
                img_h = len(img[0])

                padding = 5

                image = []
                for w in range(img_w):
                    assembly = []
                    for h in range(img_h):
                        
                        neighbors = []
                        for ww in range(w-padding, w+padding +1):
                            if 0 <= ww and ww < img_w:
                                for hh in range(h-padding, h+padding + 1):
                                    if 0 <= hh and hh < img_h:
                                        neighbors.append(img[ww][hh].copy())
                        assembly.append(a_pixel(neighbors))

                    image.append(assembly) 

            else:
                image = "None"
        else:
            image = "None"
        return image


export_nodes = [
    ReadImage,
    ShowImage,
    BlurImage,

]