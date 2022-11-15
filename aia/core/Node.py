
from .Base import Base

class Node(Base):

    def __init__(self):
        
        super().__init__()

        self.title = ''

        self.version: str = None

        self.data_inputs = list()
        self.fake_inputs = list()

        self.data_output = dict()

        self.prev_nodes = list()


    # data_inputs
    def update_data_inputs(self):
        def copy_object(obj):
            if str(type(obj)) == "<class 'list'>":
                return obj.copy()
            else:
                return obj

        self.data_inputs = list()
        for node in self.prev_nodes:
            copy_obj = copy_object(node.get_data_output("all"))
            self.data_inputs.append(copy_obj)

    def get_data_inputs(self, ind = -1):
        self.update_data_inputs()
        if ind == -1:
            return self.data_inputs
        elif ind < len(self.data_inputs):
            return self.data_inputs[ind]
        return None

    def set_fake_input(self, fake):
        self.fake_inputs = fake

    def get_fake_input(self):
        return self.fake_inputs


    # data_output
    def get_data_output(self, key = "all"):
        if key == "all":
            return self.data_output
        elif key in self.data_output.keys():
            return self.data_output[key]
        return None

    def set_data_output(self, key, obj):
        self.data_output[key] = obj

    
    # prev_nodes
    def get_prev_nodes(self, ind = -1):
        if ind == -1: # get all
            return self.prev_nodes
        elif ind < len(self.prev_nodes):
            return self.prev_nodes[ind]
        return None
    
    def push_prev_nodes(self, prev_node):
        self.prev_nodes.append(prev_node)
    
    def set_prev_nodes(self, ind, obj):
        if ind == -1:
            if str(type(obj)) == "<class 'list'>":
                self.prev_nodes = obj
            else:
                self.prev_nodes = list()
        elif ind < len(self.prev_nodes):
            self.prev_nodes[ind] = obj

    
    def remove_prev_node(self, obj):
        if obj in self.prev_nodes:
            self.prev_nodes.remove(obj)
            self.update_data_inputs()



    """ RESET """
    def reset_all(self):
        self.title = ''
        self.version: str = None

        self.data_inputs = list()

        self.data_output = dict()

        self.prev_nodes = list()  # list of input nodes