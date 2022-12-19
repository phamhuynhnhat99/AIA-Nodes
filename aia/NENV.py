import os
import argparse
from aia.core.Node import Node as Node_
from aia.gui_core.cell_op import CellOp as CellOp_


import configparser
config = configparser.ConfigParser()
config.read("config.ini")

Node = None

def init_node_env():

    parser = argparse.ArgumentParser()
    parser.add_argument('--version', dest='version', type=str, help='Get this version')
    parser.add_argument('--title', dest='title', type=str, help='Get this title')
    args = parser.parse_args()
    os.environ['VERSION'] = args.version if args.version is not None else "0"
    os.environ['TITLE'] = args.title if args.title is not None else "AIA Project"
    

    global Node

    if config["DEFAULT"]["AIA_MODE"] == 'gui':

        Node = CellOp_

    else: # config["DEFAULT"]["AIA_MODE"] == 'no-gui':
        
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