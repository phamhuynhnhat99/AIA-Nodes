from aia.NENV import *

widgets = import_widgets(__file__)

import cv2

class FaceNodeBase(Node):
    def __init__(self):
        super().__init__()
        self.image = None


    def get_output(self):
        return self.get_image()


    def update_event(self):
        self.image, all_people = self.get_output()
        self.set_data_output(key="image", obj=self.image)
        if all_people is not None:
            self.set_data_output(key="bounding boxes", obj=all_people)


class MtcnnDetector(FaceNodeBase):

    title = "Detector (MTCNN)"
    min_confidence = 0.7

    def get_image(self):

        all_people = list()
        input_0, input_1 = self.get_data_inputs(ind=0), self.get_data_inputs(ind=1)

        if input_1: # There are 2 previous nodes
            if "image" in input_1.keys():
                input = input_1
                if "output" in input_0.keys():
                    __class__.min_confidence = input_0["output"]
            else:
                input = input_0
                if "output" in input_1.keys():
                    __class__.min_confidence = input_1["output"]
        else:
            input = input_0

        if input:
            if "image" in input.keys():
                img = input["image"]

                MtcnnDetectorWidget = widgets.MtcnnDetectorWidget()
                faces = MtcnnDetectorWidget.detector.detect_faces(img)

                image = img.copy()
                color = (0, 0, 255) # red
                thickness = 2
                for face in faces:
                    if face['confidence'] > __class__.min_confidence:
                        xmin, ymin, w, h = face["box"]
                        xmax, ymax = xmin + w - 1, ymin + h - 1
                        all_people.append((xmin, ymin, xmax, ymax))
                        image = cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, thickness)

            else:
                image = None
        else:
            image = None
        return image, all_people


export_nodes = [
    MtcnnDetector,

]