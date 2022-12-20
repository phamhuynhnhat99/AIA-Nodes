from aia.NENV import *

widgets = import_widgets(__file__) # optional

import requests
import io
from PIL import Image, ImageFilter

class ImageNodeBase(Node):
    path = "image/image_nodes" # compulsory

    def __init__(self, num_inp, num_out, title):
        super().__init__(num_inp=num_inp, num_out=num_out, title=title)
        self.default_image = Image.open("aia.png")
        self.output = self.default_image
        self.does_it_use_old_output = False

    
    def get_output(self):
        return self.get_image()


    def update_event(self):
        if self.does_it_use_old_output == False:
            self.output = self.get_output()
        self.nodevalueoutput_[0] = self.output


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
    storage_folder = config["DEFAULT"]["STORAGE_FOLDER"]

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


class RemoveBackground(ImageNodeBase):
    title = "Remove Background"
    api = config["api"]["remove_background"]

    def __init__(self, num_inp=1, num_out=1, title = title):
        super().__init__(num_inp, num_out, title)

    def get_image(self):
        self.update_nodevalueinputs()
        input = self.get_nodevalueinputs(ind=0)
        if input:
            if 0 in input.keys():
                image = input[0]

                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format='PNG')
                img_byte_arr = img_byte_arr.getvalue()

                files = {'file': img_byte_arr}

                response = requests.post(__class__.api, files=files, timeout=9, verify=False) # 9 seconds
                if response.status_code == 200:
                    try:
                        imageStream = io.BytesIO(response.content)
                        image = Image.open(imageStream)
                    except requests.exceptions.RequestException:
                        print(response.text)
                else:
                    image = self.default_image
            else:
                image = self.default_image

        else:
            image = self.default_image
            
        return image


class BlurImage(ImageNodeBase):
    title = "Blur Image"
    padding = 7

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


# compulsory
export_nodes = [
    ReadImage,
    SaveImage,
    RemoveBackground,
    BlurImage,

]