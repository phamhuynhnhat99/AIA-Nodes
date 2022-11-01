import os
from aia.AIAcore.Node import Node as Node_
from aia.AIAcore.IONode import NodeInput as NodeInput_, NodeOutput as NodeOutput_


Node = None
NodeInput = None
NodeOutput = None
# dtypes = None

def init_node_env():
    global Node
    global NodeInput
    global NodeOutput
    global dtypes

    if os.environ['AIA_MODE'] == 'gui':

        pass

    else:

        Node = Node_
        NodeInput = NodeInput_
        NodeOutput = NodeOutput_
