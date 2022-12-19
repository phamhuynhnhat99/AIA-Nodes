from aia.NENV import *

widgets = import_widgets(__file__) # optional

class TextNodeBase(Node):
    path = "text/text_nodes"

    def __init__(self):
        super().__init__()
        self.output = None

    
    def get_output(self):
        return self.get_text()


    def update_event(self):
        self.output = self.get_output()
        self.nodevalueoutput_[0] = self.output


class FloatInput(TextNodeBase):
    title = "Float Input (Text)"

    def __init__(self):
        super().__init__()
        self.title = "Float Input"
        self.text = ''


    def set_tilte(self, tilte):
        self.title = tilte

    
    def get_text(self):

        FloatInputWidget = widgets.FloatInputWidget()
        FloatInputWidget.set_title(self.title)
        output = FloatInputWidget.get_float_text()

        return output


# compulsory
export_nodes = [
   FloatInput,

]