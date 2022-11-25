from aia.NENV import *

widgets = import_widgets(__file__)

class MathNodeBase(Node):
    def __init__(self, canvas, num_inp=0, num_out=1, view = "", text="Image", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, text, W, H)

    def get_output(self):
        return self.get_results()


class ConstNode(MathNodeBase):
    title = "Read Image"

    def __init__(self, canvas, num_inp=0, num_out=1, view = "", W=50, H=50):
        super().__init__(canvas, num_inp, num_out, view, __class__.title, W, H)


    def get_image(self):
        img = "/home/aia/Nhat/AIA-Nodes/test_1.png"
        return img