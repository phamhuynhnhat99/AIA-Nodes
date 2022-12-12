from aia.NENV import *

widgets = import_widgets(__file__)

from PIL import Image
import cv2, numpy

class FaceNodeBase(Node):
    path = "face/face_nodes"
    
    def __init__(self, num_inp, num_out, title):
        super().__init__(num_inp=num_inp, num_out=num_out, title=title)
        self.default_image = Image.open("aia.png")
        self.output = self.default_image


    def get_output(self):
        return self.get_image()


    def update_event(self):
        self.output, self.all_people = self.get_output()
        self.nodevalueoutput_[0] = self.output
        self.nodevalueoutput_[1] = self.all_people


class MtcnnDetector(FaceNodeBase):

    title = "Detector (MTCNN)"
    min_confidence = 0.7

    def __init__(self, num_inp=2, num_out=1, title = title):
        super().__init__(num_inp, num_out, title)

    def get_image(self):

        all_people = list()
        self.update_nodevalueinputs()
        inputs = self.get_nodevalueinputs(ind=-1) # get all inputs

        if 0 in inputs.keys():
            inputs_0 = inputs[0]
            if inputs_0 and 0 in inputs_0.keys():
                if 1 in inputs.keys() and inputs[1]:
                    if 0 in inputs[1].keys():
                        min_confidence = inputs[1][0]
                    else:
                        min_confidence = __class__.min_confidence
                else:
                    min_confidence = __class__.min_confidence

                open_cv_image = numpy.asarray(inputs_0[0])

                MtcnnDetectorWidget = widgets.MtcnnDetectorWidget()
                try:
                    faces = MtcnnDetectorWidget.detector.detect_faces(open_cv_image)
                except:
                    faces = list()

                image_clone = open_cv_image.copy()
                color = (0, 0, 255) # red
                thickness = 2
                for face in faces:
                    if face['confidence'] > min_confidence:
                        xmin, ymin, w, h = face["box"]
                        xmax, ymax = xmin + w - 1, ymin + h - 1
                        all_people.append((xmin, ymin, xmax, ymax))
                        image_clone = cv2.rectangle(image_clone, (xmin, ymin), (xmax, ymax), color, thickness)

                image = Image.fromarray(image_clone)
            
            else:
                image = self.default_image
        else:
            image = self.default_image

        return image, all_people


export_nodes = [
    MtcnnDetector,

]