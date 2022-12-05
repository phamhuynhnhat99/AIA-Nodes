import os
import sys
from aia.core.Node import Node as Node_
from aia.gui_core.cell_op import CellOp as CellOp_


Node = None


def init_node_env():
    global Node

    if os.environ['AIA_MODE'] == 'gui':

        Node = CellOp_

    else: # os.environ['AIA_MODE'] == 'no-gui':
        
        Node = Node_


def import_widgets(origin_file: str, rel_file_path='widgets.py'):

    from importlib.machinery import SourceFileLoader
    try:
        widgets_path = os.path.join(os.path.dirname(origin_file), rel_file_path)
        module_name = os.path.dirname(origin_file).split("/")[-1]
        rel_widgets = SourceFileLoader(module_name, widgets_path).load_module()
        widgets = rel_widgets.export_widgets
    except:
        widgets = None
    
    return widgets