from mtcnn.mtcnn import MTCNN

class MtcnnDetectorWidget:
    
    def __init__(self):
        self.detector = MTCNN()

    
    def detect(self, image):
        return self.detector.detect_faces(image)


class export_widgets:

    MtcnnDetectorWidget = MtcnnDetectorWidget

 