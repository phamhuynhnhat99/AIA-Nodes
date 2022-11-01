class IONode:
    def __init__(self, label: str = '', type_: str = 'data'):
        self.label: str = label
        self.type_: str = type_


class NodeInput(IONode):
    def __init__(self, label: str = '', type_: str = 'data', data=dict()):
        super().__init__(label, type_)
        self.data = data


class NodeOutput(IONode):
    def __init__(self, label: str = '', type_: str = 'data'):
        super().__init__(label, type_)
        self.data = dict()