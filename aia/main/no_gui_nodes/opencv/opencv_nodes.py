from aia.NENV import *

widgets = import_widgets(__file__)

import cv2

class Cv2NodeBase(Node):
    def __init__(self, num_inp, num_out, title):
        super().__init__(num_inp=num_inp, num_out=num_out, title=title)
        self.default_image = cv2.cvtColor(cv2.imread("aia.png"), cv2.IMREAD_COLOR)
        self.image = self.default_image

    
    def get_output(self):
        return self.get_image()


    def update_event(self):
        self.image = self.get_output()
        self.nodevalueoutput_[0] = self.image


class ReadImage(Cv2NodeBase):
    title = "Read Image (OpenCV)"

    def __init__(self, num_inp=0, num_out=1, title = title):
        super().__init__(num_inp, num_out, title)

    def get_image(self):
        readImageWidget = widgets.ReadImageWidget()
        image_path = readImageWidget.get_image_path()
        image = cv2.cvtColor(cv2.imread(image_path), cv2.IMREAD_COLOR)
        return image


class ShowImage(Cv2NodeBase):
    title = "Show Image (OpenCV)"

    def __init__(self, num_inp=1, num_out=1, title = title):
        super().__init__(num_inp, num_out, title)

    def get_image(self):
        self.update_nodevalueinputs()
        input = self.get_nodevalueinputs(ind=0)
        if input:
            print(input)
            if 0 in input.keys():
                image = input[0]
                cv2.imshow(__class__.title, image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            else:
                image = self.default_image
        else:
            image = self.default_image
            
        return image


class BlurImage(Cv2NodeBase):
    title = "Blur Image (OpenCV)"
    padding = 17

    def __init__(self, num_inp=1, num_out=1, title = title):
        super().__init__(num_inp, num_out, title)

    def get_image(self):
        self.update_nodevalueinputs()
        input = self.get_nodevalueinputs(ind=0)
        if input:
            if 0 in input.keys():
                img = input[0]
                if img is not None:
                    ksize = (__class__.padding, __class__.padding)
                    image = cv2.blur(img, ksize)
                else:
                    image = self.default_image
            else:
                image = self.default_image
        else:
            image = self.default_image

        return image


class ResizeImage(Cv2NodeBase):
    title = "Resize Image (OpenCV)"
    scale_w = 0.25
    scale_h = 0.25

    def __init__(self, num_inp=1, num_out=1, title = title):
        super().__init__(num_inp, num_out, title)

    def get_image(self):
        self.update_nodevalueinputs()
        input = self.get_nodevalueinputs(ind=0)
        if input:
            if 0 in input.keys():
                img = input[0]
                if img is not None:
                    resize_w = int(img.shape[1] * __class__.scale_w)
                    resize_h = int(img.shape[0] * __class__.scale_h)
                    dim = (resize_w, resize_h)
                    # resize image
                    image = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                else:
                    image = self.default_image
            else:
                image = self.default_image
        else:
            image = self.default_image

        return image


export_nodes = [
    ReadImage,
    ShowImage,
    BlurImage,
    ResizeImage,

]