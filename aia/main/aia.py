import os
import sys

from aia.NENV import init_node_env
from aia.flow.flow import Flow

def run():
    os.environ['AIA_MODE'] = 'no-gui'
    init_node_env()

    """ Auto loading """

    auto_loading_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "auto_loading"))
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
    order = []

    while True:
        os.system('clear')
        print("----------------------------------------")
        print("-oOo-         All of nodes         -oOo-")
        for i, node in enumerate(auto_nodes):
            print("    ", i, node.title)
        print("----------------------------------------")
        print("-oOo-       Registered Nodes       -oOo-")
        for gid, node in registered_nodes.items():
            print("    id:", gid, "   ", node.__class__.title)
        print("----------------------------------------")
        print("-oOo-     Registered Directions    -oOo-")
        for id, arrow in enumerate(arrows):
            print("    id:", id, "      ", arrow[0], '---->', arrow[1])
        print("----------------------------------------")
        print("-oOo-           Toposort           -oOo-")
        if order:
            print(order)
        else:
            print("This is not a DAG")
        print("----------------------------------------")
        print("❤️ ❤️ ❤️ ❤️ ❤️  Welcome to my world ❤️ ❤️ ❤️ ❤️ ❤️")
        print("0: Exit Program")
        print("1: Registering a new node")
        print("2: Registering a direction")
        print("3: Update a node")
        choice = input("You choice is: ")
        print("----------------------------------------")
        if choice == "1":
            ind = int(input("Node's index is: "))
            if 0 <= ind and ind < len(auto_nodes):
                new_node = auto_nodes[ind]()
                registered_nodes[new_node.global_id] = new_node

                registered_nodes[new_node.global_id].update_event()

                tmp_vertices = [gid for gid in registered_nodes.keys()]
                print(tmp_vertices, arrows)
                flow.constructor(vertices=tmp_vertices, arrows=arrows)
                order = flow.toposort()

        elif choice == "2":
            arrow = input("Enter an arrow: ").split(" ")
            u = int(arrow[0])
            v = int(arrow[1])
            if u in registered_nodes.keys() and v in registered_nodes.keys():
                if [u, v] not in arrows:
                    arrows.append([u, v])
                    registered_nodes[v].push_prev_nodes(registered_nodes[u])

                    flow.constructor(vertices=list(registered_nodes.keys()), arrows=arrows)
                    order = flow.toposort()

        elif choice == "3":
            gid = int(input("Node's Global ID is: "))
            if gid in registered_nodes.keys():
                genealogy_of_u = flow.sub_toposort_from(gid)
                for ver in genealogy_of_u:
                    registered_nodes[ver].update_event()
        else:
            break

    print("----------------------------------------")
    print("Good luck Have fun.")


if __name__ == '__main__':
    run()