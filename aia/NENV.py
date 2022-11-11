import os
import sys
from aia.core.Node import Node as Node_


Node = None


def init_node_env():
    global Node

    if os.environ['AIA_MODE'] == 'gui':

        pass

    else:
        
        Node = Node_


def import_widgets(origin_file: str, rel_file_path='widgets.py'):

    from importlib.machinery import SourceFileLoader

    widgets_path = os.path.join(os.path.dirname(origin_file), rel_file_path)
    module_name = os.path.dirname(origin_file).split("/")[-1]
    rel_widgets = SourceFileLoader(module_name, widgets_path).load_module()
    
    return rel_widgets.export_widgets


