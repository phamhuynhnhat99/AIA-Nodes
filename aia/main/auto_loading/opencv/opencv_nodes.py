from aia.NENV import *

widgets = import_widgets(__file__)

import cv2

class Cv2NodeBase(Node):
    def __init__(self):
        super().__init__()
        self.image = None

    def update_event(self):
        self.image = self.get_image()
        self.set_data_output(key="image", obj=self.image)


class ReadImage(Cv2NodeBase):
    title = "Read Image (OpenCV)"

    def get_image(self):
        # readImageWidget = widgets.ReadImageWidget()
        readImageWidget = widgets.ReadImageWidget()
        image_path = readImageWidget.get_image_path()
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        return image


class ShowImage(Cv2NodeBase):
    title = "Show Image (OpenCV)"

    def get_image(self):
        input = self.get_data_inputs(ind=0)
        if input:
            if "image" in input.keys():
                image = input["image"]

                cv2.imshow(__class__.title, image)
                cv2.waitKey(0)

            else:
                image = None
        else:
            image = None
        return image


class BlurImage(Cv2NodeBase):
    title = "Blur Image (OpenCV)"
    padding = 17

    def get_image(self):
        input = self.get_data_inputs(ind=0)
        if input:
            if "image" in input.keys():
                img = input["image"]
                if img is not None:
                    ksize = (__class__.padding, __class__.padding)
                    image = cv2.blur(img, ksize)

                else:
                    image = None
            else:
                image = None
        else:
            image = None

        return image


class ResizeImage(Cv2NodeBase):
    title = "Resize Image (OpenCV)"
    scale_w = 0.25
    scale_h = 0.25

    def get_image(self):
        input = self.get_data_inputs(ind=0)
        if input:
            if "image" in input.keys():
                img = input["image"]
                if img is not None:
                    resize_w = int(img.shape[1] * __class__.scale_w)
                    resize_h = int(img.shape[0] * __class__.scale_h)
                    dim = (resize_w, resize_h)
                    # resize image
                    image = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

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
    ResizeImage,

]