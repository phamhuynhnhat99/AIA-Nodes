import os
import sys

from aia.NENV import init_node_env
from aia.flow.flow import Flow

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
    
    flow = Flow()
    vertices = []
    arrows = []
    registered_nodes = []

    while True:
        os.system('clear')
        print("List of nodes")
        for i, node in enumerate(auto_nodes):
            print(i, node.title)
        print("----------------------------------------")
        print("-oOo-       Registered Nodes       -oOo-")
        for r_node in registered_nodes:
            print("       id:", r_node.global_id, "and title:", r_node.title)
        print("----------------------------------------")
        print("-oOo-           Vertices           -oOo-")
        if vertices:
            print(vertices)
        print("----------------------------------------")
        print("-oOo-            Arrows            -oOo-")
        for arrow in arrows:
            print("               ", arrow[0], '---->', arrow[1])
        print("----------------------------------------")
        print("<3 Welcome to my world <3")
        print("0: Exit")
        print("1: Registering a new node")
        print("2: Registering a direction")
        choice = input("You choice is: ")
        print("----------------------------------------")
        if choice == "1":
            ind = int(input("Node's index is: "))
            if 0 <= ind and ind < len(auto_nodes):
                new_node = auto_nodes[ind]()
                new_node.title = auto_nodes[ind].title
                registered_nodes.append(new_node)
                vertices.append(new_node.global_id)

        elif choice == "2":
            arrow = input("Enter an arrow: ").split(" ")
            u = int(arrow[0])
            v = int(arrow[1])
            if u in vertices and v in vertices:
                arrows.append([u, v])
        else:
            break

    flow.constructor(vertices=vertices, arrows=arrows)
    print("Toposort")
    order, end_vertices = flow.toposort()
    print(order)
    print(end_vertices)

    # read_array_ = auto_nodes[2]()
    # read_array_.read_arr()
    
    # show_array_ = auto_nodes[3]()
    # show_array_.set_prev(read_array_)
    # show_array_.show_arr()

    # selection_sort_ = auto_nodes[0]()
    # selection_sort_.set_prev(show_array_)
    # selection_sort_.update_event()

    # merge_sort_ = auto_nodes[1]()
    # merge_sort_.set_prev(show_array_)
    # merge_sort_.update_event()

    # print("Sap xep giam dan")
    # print(selection_sort_.get_data_outputs())

    # print("Sap xep tang dan")
    # print(merge_sort_.get_data_outputs())

    # print("Mang ban dau")
    # print(show_array_.get_data_outputs())

    # print(merge_sort_.global_id)

    print("__________")
    print("Good luck Have fun.")


if __name__ == '__main__':
    run()