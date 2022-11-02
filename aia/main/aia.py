import os
import sys

from aia.NENV import init_node_env

def run():
    os.environ['AIA_MODE'] = 'no-gui'
    init_node_env()

    """ Auto loading """
    par_path = os.path.abspath(os.path.join(__file__, ".."))
    auto_loading_path = os.path.abspath(os.path.join(par_path, "auto_loading"))

    auto_loading_nodes = os.listdir(auto_loading_path)

    auto_nodes = []
    for aln in auto_loading_nodes:
        aln_path = os.path.join(auto_loading_path, aln)
        sys.path.append(aln_path)
        aln_nodes = aln + "_nodes.py"
        nodes_py = os.path.join(aln_path, aln_nodes)
        auto_nodes += __import__(os.path.basename(nodes_py)[:-3]).export_nodes

    for i, node in enumerate(auto_nodes):
        print(i, node.title)
    print("_______________________________________")



    read_array_ = auto_nodes[1]()
    read_array_.read_arr()
    
    show_array_ = auto_nodes[2]()
    show_array_.set_prev(read_array_)
    print(show_array_.get_arr())
    print(show_array_.get_data_outputs())



    print("__________")
    print("Good luck Have fun.")


if __name__ == '__main__':
    run()