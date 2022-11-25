from aia.NENV import *

widgets = import_widgets(__file__)

from PIL import Image, ImageFilter

class ImageNodeBase(Node):
    def __init__(self, canvas, num_inp=0, num_out=1, view = "", text="Image", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, text, W, H)

    
    def get_image_from_str_or_img(self, img):
        if str(type(img)) == "<class 'str'>":
            image = Image.open(img)
        elif str(type(img)) == "<class 'PIL.Image.Image'>":
            image = img
        else:
            image = Image.open("/home/aia/Nhat/AIA-Nodes/aia.png")
        return image


    def get_output(self):
        return self.get_image()


class ReadImage(ImageNodeBase):
    title = "Read Image"

    def __init__(self, canvas, num_inp=0, num_out=1, view = "", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, __class__.title, W, H)


    def get_image(self):
        img = "/home/aia/Nhat/AIA-Nodes/test_1.png"
        return img


class ShowImage(ImageNodeBase):
    title = "Show Image"

    def __init__(self, canvas, num_inp=1, num_out=1, view = "", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, __class__.title, W, H)

    def get_image(self):
        if 0 in self.cellinputs.keys():
            img = self.get_image_from_str_or_img(self.cellinputs[0].cellvalueoutput_.value)
        else:
            img = self.get_image_from_str_or_img(None)

        w, h = img.size
        scale = (self.W if self.W < self.H else self.H) / (w if w > h else h)
        new_w, new_h = int(scale * w), int(scale * h)
        new_size = (new_w, new_h)
        img = img.resize(new_size)

        return img


class ReadImageClone(ImageNodeBase):
    title = "Read Image Clone"

    def __init__(self, canvas, num_inp=0, num_out=1, view = "", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, __class__.title, W, H)
        

    def get_image(self):
        img = "/home/aia/Nhat/AIA-Nodes/test_2.png"
        return img


class BlurImage(ImageNodeBase):
    title = "Blur Image"

    def __init__(self, canvas, num_inp=1, num_out=1, view = "", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, __class__.title, W, H)

    def get_image(self):
        if 0 in self.cellinputs.keys():
            img = self.get_image_from_str_or_img(self.cellinputs[0].cellvalueoutput_.value)
        else:
            img = self.get_image_from_str_or_img(None)
        img = img.filter(ImageFilter.BLUR)

        return img