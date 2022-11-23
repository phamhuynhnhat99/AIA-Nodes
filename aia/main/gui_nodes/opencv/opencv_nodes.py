from aia.NENV import *

widgets = import_widgets(__file__)

import cv2
from PIL import Image, ImageTk

class Cv2NodeBase(Node):
    def __init__(self, canvas, num_inp=0, num_out=1, view = "", text="Cv2", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, text, W, H)
        self.output_ = dict()

    def get_output(self):
        return self.get_image()


class ReadImage(Cv2NodeBase):
    title = "Read Image (OpenCV)"

    def __init__(self, canvas, num_inp=0, num_out=1, view = "", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, __class__.title, W, H)

    def get_image(self):
        img = Image.open("/home/aia/Nhat/AIA-Nodes/Test_1.jpg")
        w, h = img.size
        scale = 400 / (w if w > h else h)
        new_w, new_h = int(scale * w), int(scale * h)
        new_size = (new_w, new_h)
        img = ImageTk.PhotoImage(img.resize(new_size))
        return img


class ShowImage(Cv2NodeBase):
    title = "Show Image (OpenCV)"

    def __init__(self, canvas, num_inp=1, num_out=1, view = "", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, __class__.title, W, H)

    def get_image(self):
        if len(self.cellinputs) > 0:
            image = self.cellinputs[0].output_.value
        else:
            image = None
        return image


export_nodes = [
    ReadImage,
    ShowImage,

]