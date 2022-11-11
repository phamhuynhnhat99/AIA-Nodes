from aia.NENV import *

widgets = import_widgets(__file__)

from mtcnn import MTCNN
import cv2

class FaceNodeBase(Node):
    def __init__(self):
        super().__init__()
        self.image = None

    def update_event(self):
        self.image, detector = self.get_image()
        self.set_data_output(key="image", obj=self.image)
        if detector is not None:
            self.set_data_output(key="detector", obj=detector)


class Detector(FaceNodeBase):

    title = "Detector (MTCNN)"
    detector = MTCNN()

    min_confidence = 0.6

    def get_image(self):

        all_people = list()
        input = self.get_data_inputs(ind=0)
        if input:
            if "image" in input.keys():
                image = input["image"]

                faces = __class__.detector.detect_faces(image)

                color = (0, 255, 0)
                thickness = 2
                detector = []
                for face in faces:
                    if face['confidence'] > __class__.min_confidence:
                        xmin, ymin, w, h = face["box"]
                        xmax, ymax = xmin + w - 1, ymin + h - 1
                        detector.append((xmin, ymin, xmax, ymax))
                        image = cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, thickness)

            else:
                image = None
        else:
            image = None
        return image, detector


export_nodes = [
    Detector,

]