from aia.NENV import *

widgets = import_widgets(__file__)

from PIL import Image, ImageFilter

class ImageNodeBase(Node):
    path = "image/image_nodes"

    def __init__(self, num_inp, num_out, title):
        super().__init__(num_inp=num_inp, num_out=num_out, title=title)
        self.default_image = Image.open("aia.png")
        self.image = self.default_image

    
    def get_output(self):
        return self.get_image()


    def update_event(self):
        self.image = self.get_output()
        self.nodevalueoutput_[0] = self.image


class ReadImage(ImageNodeBase):
    title = "Read Image"

    def __init__(self, num_inp=0, num_out=1, title = title):
        super().__init__(num_inp, num_out, title)

    def get_image(self):
        readImageWidget = widgets.ReadImageWidget()
        image_path = readImageWidget.get_image_path()
        image = Image.open(image_path)
        return image


class SaveImage(ImageNodeBase):
    title = "Save Image"
    storage_folder = os.environ["STORAGE_FOLDER"]

    def __init__(self, num_inp=1, num_out=1, title = title):
        super().__init__(num_inp, num_out, title)

    def get_image(self):
        self.update_nodevalueinputs()
        input = self.get_nodevalueinputs(ind=0)
        if input:
            if 0 in input.keys():
                image = input[0]
                image_name = str(self.global_id) + ".png"
                storage_version_folder = __class__.storage_folder + os.environ['VERSION']
                image_path = os.path.join(storage_version_folder, image_name)
                if not os.path.isdir(storage_version_folder):
                    os.mkdir(storage_version_folder)
                image.save(image_path)
            else:
                image = self.default_image
        else:
            image = self.default_image
        return image


# class ShowImage(ImageNodeBase):
#     title = "Show Image"

#     def __init__(self, num_inp=1, num_out=1, title = title):
#         super().__init__(num_inp, num_out, title)

#     def get_image(self):
#         self.update_nodevalueinputs()
#         input = self.get_nodevalueinputs(ind=0)
#         if input:
#             print(input)
#             if 0 in input.keys():
#                 image = input[0]
#                 image.show()
#             else:
#                 image = self.default_image
#         else:
#             image = self.default_image
            
#         return image


class BlurImage(ImageNodeBase):
    title = "Blur Image"
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
                    image = img.filter(ImageFilter.GaussianBlur(__class__.padding))
                else:
                    image = self.default_image
            else:
                image = self.default_image
        else:
            image = self.default_image

        return image


export_nodes = [
    ReadImage,
    SaveImage,
    # ShowImage,
    BlurImage,

]