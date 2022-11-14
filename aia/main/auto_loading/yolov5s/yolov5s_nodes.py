from aia.NENV import *

widgets = import_widgets(__file__)

import cv2

class Yolov5sNodeBase(Node):
    def __init__(self):
        super().__init__()
        self.image = None

    def update_event(self):
        self.image, all_people = self.get_image()
        self.set_data_output(key="image", obj=self.image)
        if all_people is not None:
            self.set_data_output(key="bounding boxes", obj=all_people)


class Yolov5sDetector(Yolov5sNodeBase):

    title = "Detector (Yolov5s)"
    min_confidence = 0.99

    def get_image(self):

        all_people = list()
        input_1 = self.get_data_inputs(ind=0)
        input_2 = self.get_data_inputs(ind=1)

        if input_2: # There are 2 previous nodes
            if "image" in input_2.keys():
                input = input_2
                if "output" in input_1.keys():
                    __class__.min_confidence = input_1["output"]
            else:
                input = input_1
                if "output" in input_2.keys():
                    __class__.min_confidence = input_2["output"]
        else:
            input = input_1


        if input:
            if "image" in input.keys():
                image = input["image"]

                Yolov5sWidget = widgets.Yolov5sWidget()
                predict_df = Yolov5sWidget.get_predict_df(image)
                person_df = predict_df.loc[predict_df['class'] == 0] # human

                for index, person in person_df.iterrows():
                    if person['confidence'] >= __class__.min_confidence:
                        xmin, xmax = int(person.xmin), int(person.xmax)
                        ymin, ymax = int(person.ymin), int(person.ymax)
                        all_people.append((xmin, ymin, xmax, ymax))

                color = (255, 0, 0) # blue
                thickness = 2
                for xmin, ymin, xmax, ymax in all_people:
                    image = cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, thickness)

            else:
                image = None
        else:
            image = None
        return image, all_people


export_nodes = [
    Yolov5sDetector,

]