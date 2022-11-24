from aia.NENV import *

widgets = import_widgets(__file__)

from PIL import Image

class ImageNodeBase(Node):
    def __init__(self, canvas, num_inp=0, num_out=1, view = "", text="Cv2", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, text, W, H)
        self.output_ = dict()

    def get_output(self):
        return self.get_image()


class ReadImage(ImageNodeBase):
    title = "Read Image"

    def __init__(self, canvas, num_inp=0, num_out=1, view = "", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, __class__.title, W, H)


    def get_image(self):
        img = Image.open("/home/aia/Nhat/AIA-Nodes/test_1.png")
        return img


class ReadImageClone(ImageNodeBase):
    title = "Read Image Clone"

    def __init__(self, canvas, num_inp=0, num_out=1, view = "", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, __class__.title, W, H)
        

    def get_image(self):
        img = Image.open("/home/aia/Nhat/AIA-Nodes/test_2.png")
        return img


class ShowImage(ImageNodeBase):
    title = "Show Image"

    def __init__(self, canvas, num_inp=1, num_out=1, view = "", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, __class__.title, W, H)

    def get_image(self):
        try:
            img = self.cellinputs[0].cellvalueoutput_.value
        except:
            img = Image.open("/home/aia/Nhat/AIA-Nodes/aia.png")

        w, h = img.size
        scale = (self.W if self.W < self.H else self.H) / (w if w > h else h)
        new_w, new_h = int(scale * w), int(scale * h)
        new_size = (new_w, new_h)
        img = img.resize(new_size)

        return img


export_nodes = [
    ReadImage,
    ShowImage,

]