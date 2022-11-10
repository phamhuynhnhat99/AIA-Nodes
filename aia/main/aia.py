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
        try:
            auto_nodes += __import__(os.path.basename(nodes_py)[:-3]).export_nodes
        except:
            continue
    
    flow = Flow()
    arrows = []
    registered_nodes = dict()

    # """ Debug """
    # auto_nodes[0]().get_image()
    # return

    while True:
        os.system('clear')
        print("List of nodes")
        for i, node in enumerate(auto_nodes):
            print(i, node.title)
        print("----------------------------------------")
        print("-oOo-       Registered Nodes       -oOo-")
        for gid, node in registered_nodes.items():
            print("       id:", gid, "and title:", node.__class__.title)
        print("----------------------------------------")
        print("-oOo-            Arrows            -oOo-")
        for arrow in arrows:
            print("              ", arrow[0], '---->', arrow[1])
        print("----------------------------------------")
        print("❤️  Welcome to my world ❤️")
        print("0: Exit")
        print("1: Registering a new node")
        print("2: Registering a direction")
        choice = input("You choice is: ")
        print("----------------------------------------")
        if choice == "1":
            ind = int(input("Node's index is: "))
            if 0 <= ind and ind < len(auto_nodes):
                new_node = auto_nodes[ind]()
                registered_nodes[new_node.global_id] = new_node

        elif choice == "2":
            arrow = input("Enter an arrow: ").split(" ")
            u = int(arrow[0])
            v = int(arrow[1])
            if u in registered_nodes.keys() and v in registered_nodes.keys():
                arrows.append([u, v])
                registered_nodes[v].push_prev_nodes(registered_nodes[u])
        else:
            break

    flow.constructor(vertices=list(registered_nodes.keys()), arrows=arrows)
    order, end_vertices = flow.toposort()

    if order:
        print("Toposort")
        print(order)
        print("----------------------------------------")
        for ver in order:
            if not ver in end_vertices:
                registered_nodes[ver].update_event()
        
        print("All of End Vertices")
        print(end_vertices)
        print("----------------------------------------")
        for ver in end_vertices:
            registered_nodes[ver].update_event()

    else:
        print("This is not a DAG, dude")

    print("----------------------------------------")
    print("Good luck Have fun.")


if __name__ == '__main__':
    run()