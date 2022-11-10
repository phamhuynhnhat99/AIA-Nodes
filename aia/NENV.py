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
    """
    Import all exported widgets from 'widgets.py' with respect to the origin_file location.
    Returns an object with all exported widgets as attributes for direct access.
    """

    dir_location = os.path.dirname(origin_file)
    abs_widgets_path = os.path.join(dir_location, rel_file_path)

    sys.path.append(dir_location)
    widgets = __import__("widgets").export_widgets

    return widgets