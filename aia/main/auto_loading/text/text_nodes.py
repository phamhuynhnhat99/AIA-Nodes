from aia.NENV import *

widgets = import_widgets(__file__)

class TextNodeBase(Node):

    def __init__(self):
        super().__init__()
        self.output = None

    def update_event(self):
        self.output = self.get_output()
        self.set_data_output(key="output", obj=self.output)


class FloatInput(TextNodeBase):
    title = "Float Input (Text)"

    def __init__(self):
        super().__init__()
        self.title = "Float Input"
        self.text = ''


    def set_tilte(self, tilte):
        self.title = tilte

    
    def get_output(self):

        FloatInputWidget = widgets.FloatInputWidget()
        FloatInputWidget.set_title(self.title)
        output = FloatInputWidget.get_float_text()

        return output


export_nodes = [
   FloatInput,

]