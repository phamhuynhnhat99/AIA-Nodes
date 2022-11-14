from aia.NENV import *

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class ImageNodeBase(Node):

    def __init__(self):
        super().__init__()
        self.image = None

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
                initialdir='/home/',
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
                image = None
        else:
            image = None
        return image


class BlurImage(ImageNodeBase):
    title = "Blur Image"
    padding = 17

    def get_image(self):

        def rgb_plus(pixel_1, pixel_2):
            try:
                pixel_res = [int(_1) + int(_2) for _1, _2 in zip(pixel_1, pixel_2)]
            except:
                pixel_res = [0, 0, 0]
            return pixel_res

        def rgb_sub(pixel_1, pixel_2):
            try:
                pixel_res = [int(_1) - int(_2) for _1, _2 in zip(pixel_1, pixel_2)]
            except:
                pixel_res = [0, 0, 0]
            return pixel_res

        def rgb_divide(pixel, num):
            try:
                pixel_res = [int(int(_) / num) for _ in pixel]
            except:
                pixel_res = [0, 0, 0]
            return pixel_res

        def get_min_or_max(a, b, get_min=True):
            if get_min:
                if a < b:
                    return a
                return b
            else:
                if a > b:
                    return a
                return b


        input = self.get_data_inputs(ind=0)
        if input:
            if "image" in input.keys():
                img = input["image"]
                if img is not None:
                    img_w = len(img)
                    img_h = len(img[0])
                    padding = __class__.padding

                    r = lambda: [None]*img_h
                    f = [r() for _ in range(img_w)]

                    f[0][0] = img[0][0].copy()

                    w = 0
                    for h in range(1, img_h):
                        f[w][h] = rgb_plus(img[w][h], f[w][h-1])

                    h = 0
                    for w in range(1, img_w):
                        f[w][h] = rgb_plus(img[w][h], f[w-1][h])

                    for w in range(1, img_w):
                        for h in range(1, img_h):
                            tmp = rgb_plus(f[w-1][h], f[w][h-1])
                            tmp = rgb_sub(tmp, f[w-1][h-1])
                            f[w][h] = rgb_plus(tmp, img[w][h])
                    
                    image = [r() for _ in range(img_w)]
                    for w in range(img_w):
                        for h in range(img_h):
                            min_w = get_min_or_max(w-padding, 0, get_min=False)
                            max_w = get_min_or_max(w+padding, img_w-1, get_min=True)
                            min_h = get_min_or_max(h-padding, 0, get_min=False)
                            max_h = get_min_or_max(h+padding, img_h-1, get_min=True)

                            rgb = f[max_w][max_h].copy()

                            if min_w - 1 >= 0:
                                rgb = rgb_sub(rgb, f[min_w-1][max_h])

                            if min_w - 1 >= 0 and min_h - 1 >= 0:
                                rgb = rgb_plus(rgb, f[min_w-1][min_h-1])

                            if min_h - 1 >= 0:
                                rgb = rgb_sub(rgb, f[max_w][min_h-1])

                            num_pixels = (max_w-min_w+1) * (max_h-min_h+1)
                            image[w][h] = rgb_divide(pixel=rgb, num=num_pixels)
                    
                else:
                    image = None
            else:
                image = None
        else:
            image = None

        return image


export_nodes = [
    ReadImage,
    ShowImage,
    BlurImage,

]