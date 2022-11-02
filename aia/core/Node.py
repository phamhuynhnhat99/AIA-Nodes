
from .Base import Base

class Node(Base):

    def __init__(self):
        super().__init__()

        self.title = ''
        self.version: str = None

        self.data_inputs = list()
        self.data_outputs = list()
        self.prev_nodes = list()

    # data_inputs
    def get_data_inputs(self, type = -1):
        if type == -1:
            return self.data_inputs
        elif type < len(self.data_inputs):
            return self.data_inputs[type]
        return None

    def push_data_inputs(self, obj):
        self.data_inputs.append(obj)

    def set_data_inputs(self, type, obj):
        if type == -1:
            self.data_outputs = obj
        elif type < len(self.data_outputs):
            self.data_outputs[type] = obj

    # data_outputs
    def get_data_outputs(self, type = -1):
        if type == -1:
            return self.data_outputs
        elif type < len(self.data_outputs):
            return self.data_outputs[type]
        return None

    def push_data_outputs(self, obj):
        self.data_outputs.append(obj)

    def set_data_outputs(self, type, obj):
        if type == -1:
            self.data_outputs = obj
        elif type < len(self.data_outputs):
            self.data_outputs[type] = obj
    
    # prev_nodes
    def get_prev_nodes(self, type = -1):
        if type == -1: # get all
            return self.prev_nodes
        elif type < len(self.prev_nodes):
            return self.prev_nodes[type]
        return None
    
    def push_prev_nodes(self, prev_node):
        self.prev_nodes.append(prev_node)
    
    def set_prev_nodes(self, type, obj):
        if type == -1:
            self.prev_nodes = obj
        elif type < len(self.prev_nodes):
            self.prev_nodes[type] = obj


    """ RESET """
    def reset_all(self):
        self.title = ''
        self.version: str = None

        self.data_inputs = list()
        self.data_outputs = list()
        self.prev_nodes = list()  # list of input nodes