import os
import sys

class GUI_utils:

    def __init__(self):
        self.gui_nodes = []

    
    def auto_loading(self):
        """ Load all of nodes that from aia.main.auto_loading folder """
        auto_loading_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "gui_nodes"))
        auto_loading_nodes = os.listdir(auto_loading_path)
        for aln in auto_loading_nodes:
            aln_path = os.path.join(auto_loading_path, aln)
            sys.path.append(aln_path)
            aln_nodes = aln + "_nodes.py"
            nodes_py = os.path.join(aln_path, aln_nodes)
            try:
                self.gui_nodes += __import__(os.path.basename(nodes_py)[:-3]).export_nodes
            except:
                continue


class export_widgets:

    GUI_utils = GUI_utils