

from .Base import Base

class Node(Base):

    title = ''

    version: str = None

    init_inputs = list()  # list of NodeInputType

    init_outputs = list()  # list of NodeOutputType

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

        self.inputs = list()  # list of NodeInput
        self.outputs = list()  # list of NodeOutput
