
from .Base import Base

class Node(Base):

    title = ''

    version: str = None

    node_inputs = list()  # list of input nodes

    node_outputs = list()  # list of outputs node

    identifier: str = None

    legacy_identifiers = list()  # list of compatible identifiers

    identifier_prefix: str = None

    """
    Initialization
    """

    @classmethod
    def _build_identifier(cls):

        prefix = ''
        if cls.identifier_prefix is not None:
            prefix = cls.identifier_prefix + '.'

        if cls.identifier is None:
            cls.identifier = cls.__name__

        cls.identifier = prefix + cls.identifier


    def __init__(self):
        Base.__init__(self)

        self.data_inputs = list()
        self.data_outputs = list()

    def get_inputs(self):
        return self.data_inputs

    def push_inputs(self, data):
        self.data_inputs.append(data)

    def get_outputs(self):
        return self.data_outputs

    def push_outputs(self, data):
        self.data_outputs.append(data)

    def set_outputs(self, type, data):
        if type == -1:
            self.data_outputs = data
        elif type < len(self.data_outputs):
            self.data_outputs[type] = data