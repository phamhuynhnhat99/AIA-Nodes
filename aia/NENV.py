import os
from aia.core.Node import Node as Node_


Node = None


def init_node_env():
    global Node

    if os.environ['AIA_MODE'] == 'gui':

        pass

    else:
        print("Good way")
        print("----------")
        Node = Node_

