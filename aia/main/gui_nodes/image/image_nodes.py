from aia.NENV import *

widgets = import_widgets(__file__)

import requests
import io
from PIL import Image, ImageFilter, ImageTk
from tkinter import filedialog

class ImageNodeBase(Node):

    def __init__(self, canvas, num_inp=0, num_out=1, view = "", text="Image", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, text, W, H)

    
    def image_or_default(self, img):
        if img == None:
            image = self.default_image
        else:
            image = img
        return image

    
    def update_on_canvas(self):
        return self.get_update_time()


    def get_output(self):
        return self.get_image()


# ------------------------------------------------------------------------------------------


class ReadImage(ImageNodeBase):
    title = "Read Image"

    def __init__(self, canvas, num_inp=0, num_out=1, view = "", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, __class__.title, W, H)

    
    def button_clicked(self):
        filetypes = (
            ('All files', '*.*'),
            ('jpg files', '*.jpg'),
            ('png files', '*.png'),
        )
        self.file_path = filedialog.askopenfilename(
            title='Choose a file',
            initialdir='/home/',
            filetypes=filetypes)
        if not self.file_path:
            self.file_path = self.default_image_path
        self.update()

    
    def get_update_time(self):
        self.canvas.itemconfig(self.IDtext, text=self.file_path)
        return 1000


    def get_image(self):
        image = Image.open(self.file_path)
        return image


class ShowImage(ImageNodeBase):
    title = "Show Image"

    def __init__(self, canvas, num_inp=1, num_out=1, view = "", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, __class__.title, W, H)

    
    def get_update_time(self):

        img = self.cellvalueoutput_.value

        if img is None or img == 0:
            img = self.default_image

        w, h = img.size
        scale = (self.W if self.W < self.H else self.H) / (w if w > h else h)
        new_w, new_h = int(scale * w), int(scale * h)
        new_size = (new_w, new_h)
        img = img.resize(new_size)

        self.current_img = ImageTk.PhotoImage(img)
        self.canvas.itemconfig(self.ID, image=self.current_img)
        return 1000


    def get_image(self):
        if 0 in self.cellinputs.keys():
            img = self.image_or_default(self.cellinputs[0].cellvalueoutput_.value)
        else:
            img = self.image_or_default(None)

        return img


class BlurImage(ImageNodeBase):
    title = "Blur Image"

    def __init__(self, canvas, num_inp=1, num_out=1, view = "", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, __class__.title, W, H)

    
    def get_update_time(self):
        # do Sth
        return 1000


    def get_image(self):
        if 0 in self.cellinputs.keys():
            img = self.image_or_default(self.cellinputs[0].cellvalueoutput_.value)
            img = img.filter(ImageFilter.BLUR)
        else:
            img = self.image_or_default(None)
        return img

    
class RemoveBackground(ImageNodeBase):

    title = "Remove Background"

    api = 'https://118.69.190.178:5000/remove'

    def __init__(self, canvas, num_inp=1, num_out=1, view = "", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, __class__.title, W, H)

    
    def get_update_time(self):
        # do Sth
        return 10000


    def get_image(self):
        if 0 in self.cellinputs.keys():
            img = self.image_or_default(self.cellinputs[0].cellvalueoutput_.value)
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            
            files = {'file': img_byte_arr}

            response = requests.post(__class__.api, files=files, timeout=9, verify=False) # 9 seconds
            if response.status_code == 200:
                try:
                    imageStream = io.BytesIO(response.content)
                    img = Image.open(imageStream)
                except requests.exceptions.RequestException:
                    print(response.text)
            else:
                img = self.image_or_default(None)
        else:
            img = self.image_or_default(None)
        return img