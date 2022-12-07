import os
import sys

from aia.flow.flow import Flow

import matplotlib.pyplot as plt
import networkx as nx

class Coordinator:

    def __init__(self):
        # Topo
        self.flow = Flow()

        # all of nodes that may be used
        self.no_gui_nodes = []

        # all of directions
        self.arrows = []

        # Contain nodes that are registered from self.no_gui_nodes
        self.registered_nodes = dict() # key = gid, value = Node

        # Toposort Result
        self.order = []

    
    def auto_loading(self):
        """ Load all of nodes that from aia.main.auto_loading folder """
        auto_loading_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "no_gui_nodes"))
        auto_loading_nodes = os.listdir(auto_loading_path)
        try:
            auto_loading_nodes.remove("__pycache__")
        except:
            None
        for aln in auto_loading_nodes:
            aln_path = os.path.join(auto_loading_path, aln)
            sys.path.append(aln_path)
            aln_nodes = aln + "_nodes.py"
            nodes_py = os.path.join(aln_path, aln_nodes)
            try:
                module_name = os.path.basename(nodes_py).split(".py")[0]
                self.no_gui_nodes += __import__(module_name).export_nodes
            except:
                continue


    def display_no_gui_nodes(self):
        print("-oOo-         All of nodes         -oOo-")
        for i, node_class in enumerate(self.no_gui_nodes):
            print("    Index:", i, "   ", node_class.title)

    
    def display_registered_nodes(self):
        for gid, node in self.registered_nodes.items():
            print("    id:", gid, "   ", node.__class__.title)


    def display_arrows(self):

        G = nx.DiGraph()
        plt.clf()

        visited = []

        for id, arrow in enumerate(self.arrows):
            print("             ", arrow[0], '---->', arrow[1])

            u_gid = arrow[0]
            v_gid = arrow[1]
            u_title = self.registered_nodes[u_gid].__class__.title
            v_title = self.registered_nodes[v_gid].__class__.title
            G.add_edge(str(u_gid) + "\n" + u_title, str(v_gid) + "\n" + v_title)
            if u_gid not in visited:
                visited.append(u_gid)
            if v_gid not in visited:
                visited.append(v_gid)
        
        for ver, node in self.registered_nodes.items():
            if ver not in visited:
                ver_name = str(ver) + "\n" + node.__class__.title
                G.add_node(ver_name)
        
        nx.draw(G, with_labels=True, node_size=50, node_color='cyan', font_color='red', edgecolors='k', width=2.0)
        plt.savefig('Graph Networkx.png')

    
    def display_order(self):
        if self.order != []:
            print(self.order)
        else:
            print("This is not a DAG")

    
    def updating_toposort(self):
        tmp_vertices = list(self.registered_nodes.keys())
        self.flow.update_graph(vertices=tmp_vertices, arrows=self.arrows)
        self.order = self.flow.toposort()

    
    def updating_a_registered_node(self, gid):
        """ get its descendants and "update_event" all of them """
        if gid in self.registered_nodes.keys():
            if self.order is not None: # Topo Existing
                genealogy_of_u = self.flow.sub_toposort_from(gid)
                for v in genealogy_of_u:
                    self.registered_nodes[v].update_event()


    def registering_a_new_node(self, ind):
        if 0 <= ind and ind < len(self.no_gui_nodes):
            new_node = self.no_gui_nodes[ind]()
            self.registered_nodes[new_node.global_id] = new_node
            # self.registered_nodes[new_node.global_id].update_event()
            self.updating_toposort()
            

    def registering_a_new_arrow(self, u, v, ind):
        if u in self.registered_nodes.keys() and v in self.registered_nodes.keys():

            if ind in self.registered_nodes[v].nodeinputs.keys():
                if self.registered_nodes[v].nodeinputs[ind] is not None:
                    old_u = self.registered_nodes[v].nodeinputs[ind].global_id
                    self.arrows.remove([old_u, v])
                del self.registered_nodes[v].nodeinputs[ind]

            if ind in self.registered_nodes[v].nodevalueinputs.keys():
                del self.registered_nodes[v].nodevalueinputs[ind]

            if u != v:
                if [u, v] not in self.arrows:
                    self.arrows.append([u, v])
                    self.registered_nodes[v].nodeinputs[ind] = self.registered_nodes[u]

                    self.updating_toposort()
                    # get vertex v's descendants and "update_event()" all of them
                    self.updating_a_registered_node(v)


    def removing_a_registered_node(self, gid):
        if gid in self.registered_nodes.keys():

            # get vertex's descendants (before vertex will be removed)
            genealogy_of_u = self.flow.sub_toposort_from(gid)
            
            # get arrows that contain gid (vertex)
            sub_arrows = [arrow for arrow in self.arrows if gid in arrow]
            for arrow in sub_arrows:
                u = arrow[0] # u is gid or
                v = arrow[1] # or v is gid
                self.registered_nodes[v].remove_nodeinputs_and_its_value(self.registered_nodes[u])
                self.arrows.remove(arrow)

            # Delete node
            del self.registered_nodes[gid]

            self.updating_toposort()
            # Update its descendants
            for ver in genealogy_of_u:
                if ver != gid:
                    self.registered_nodes[ver].update_event()
            

    def removing_a_registered_arrow(self, u, v):
        if [u, v] in self.arrows:
            self.arrows.remove([u, v])
            self.registered_nodes[v].remove_nodeinputs_and_its_value(self.registered_nodes[u])

            self.updating_toposort()
            # get vertex v's descendants and "update_event" all of them
            self.updating_a_registered_node(v)


class export_widgets:

    Coordinator = Coordinator