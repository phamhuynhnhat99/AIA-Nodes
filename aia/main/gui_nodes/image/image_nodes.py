from aia.NENV import *

widgets = import_widgets(__file__)

from PIL import Image, ImageFilter, ImageTk

class ImageNodeBase(Node):
    def __init__(self, canvas, num_inp=0, num_out=1, view = "", text="Image", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, text, W, H)

    
    def get_image_from_str_or_img(self, img):
        if img == None:
            image = Image.open("/home/aia/Nhat/AIA-Nodes/aia.png")
        if str(type(img)) == "<class 'str'>":
            image = Image.open(img)
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

    
    def get_update_time(self):
        # do Sth
        return 2000


    def get_image(self):
        img = "/home/aia/Nhat/AIA-Nodes/test_1.png"
        return img


class ShowImage(ImageNodeBase):
    title = "Show Image"

    def __init__(self, canvas, num_inp=1, num_out=1, view = "", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, __class__.title, W, H)

    
    def get_update_time(self):

        img = self.cellvalueoutput_.value

        if img is None or img == 0:
            img = Image.open("/home/aia/Nhat/AIA-Nodes/aia.png")

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
            img = self.get_image_from_str_or_img(self.cellinputs[0].cellvalueoutput_.value)
        else:
            img = self.get_image_from_str_or_img(None)

        return img


class ReadImageClone(ImageNodeBase):
    title = "Read Image Clone"

    def __init__(self, canvas, num_inp=0, num_out=1, view = "", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, __class__.title, W, H)

    
    def get_update_time(self):
        # do Sth
        return 2000
        

    def get_image(self):
        img = "/home/aia/Nhat/AIA-Nodes/test_2.png"
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
            img = self.get_image_from_str_or_img(self.cellinputs[0].cellvalueoutput_.value)
        else:
            img = self.get_image_from_str_or_img(None)
        img = img.filter(ImageFilter.BLUR)

        return img