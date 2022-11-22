from aia.NENV import *

widgets = import_widgets(__file__)

import cv2

class Cv2NodeBase(Node):
    def __init__(self, canvas, num_inp=0, num_out=1, text="Cv2", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, text, W, H)
        self.output_ = dict()

    def get_output(self):
        return self.get_image()


class ReadImage(Cv2NodeBase):
    title = "Read Image (OpenCV)"

    def __init__(self, canvas, num_inp=0, num_out=1, W=50, H=50):
        super().__init__(canvas, num_inp, num_out, __class__.title, W, H)

    def get_image(self):
        return 1999
        readImageWidget = widgets.ReadImageWidget()
        image_path = readImageWidget.get_image_path()
        image = cv2.cvtColor(cv2.imread(image_path), cv2.IMREAD_COLOR)
        return image


class ShowImage(Cv2NodeBase):
    title = "Show Image (OpenCV)"

    def __init__(self, canvas, num_inp=1, num_out=1, W=50, H=50):
        super().__init__(canvas, num_inp, num_out, __class__.title, W, H)

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