import os
import sys
import json

from aia.flow.flow import Flow

import matplotlib.pyplot as plt
import networkx as nx

class Coordinator:

    def __init__(self):

        self.title = os.environ["TITLE"]
        self.version = os.environ["VERSION"]

        # Topo
        self.flow = Flow()

        # all of nodes that may be used
        self.no_gui_nodes = []

        # all of directions
        self.arrows = []
        self.locations = dict() # example: self.locations[(0, 1)] = 1 means vertex 1 were connected with 0 via port 1

        # Contain nodes that are registered from self.no_gui_nodes
        self.registered_nodes = dict() # key = gid, value = Node

        # Toposort Result
        self.order = []

    
    def reset(self):
        self.title = os.environ["TITLE"]
        self.version = os.environ["VERSION"]
        self.flow = Flow()
        self.no_gui_nodes = []
        self.arrows = []
        self.locations = dict()
        self.registered_nodes = dict()
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

        for arrow in self.arrows:
            print("             ", arrow[0], '---->', arrow[1], 'at (', self.locations[(arrow[0], arrow[1])], ')')

            u_gid = arrow[0]
            v_gid = arrow[1]
            u_title = self.registered_nodes[u_gid].__class__.title
            v_title = self.registered_nodes[v_gid].__class__.title
            u_name = str(u_gid)
            for _ in u_title.split(" "):
                u_name = u_name + "\n" + _
            v_name = str(v_gid)
            for _ in v_title.split(" "):
                v_name = v_name + "\n" + _
            G.add_edge(u_name, v_name)
            if u_gid not in visited:
                visited.append(u_gid)
            if v_gid not in visited:
                visited.append(v_gid)
        
        for ver, node in self.registered_nodes.items():
            if ver not in visited:
                ver_name = str(ver)
                for _ in node.__class__.title.split(" "):
                    ver_name = ver_name + "\n" + _
                G.add_node(ver_name)
        
        nx.draw(G, with_labels=True, node_size=11, node_color='#e6e6fa', font_color='#990000', font_size=7, edgecolors='k', width=1.7)
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
                    del self.locations[(old_u, v)]
                del self.registered_nodes[v].nodeinputs[ind]

            if ind in self.registered_nodes[v].nodevalueinputs.keys():
                del self.registered_nodes[v].nodevalueinputs[ind]

            if u != v:
                if [u, v] not in self.arrows:
                    self.arrows.append([u, v])
                    self.locations[(u, v)] = ind
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
                del self.locations[(u, v)]

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
            del self.locations[(u, v)]
            self.registered_nodes[v].remove_nodeinputs_and_its_value(self.registered_nodes[u])

            self.updating_toposort()
            # get vertex v's descendants and "update_event" all of them
            self.updating_a_registered_node(v)


    def save(self):
        self.save = dict()

        """ general info """
        self.save["general info"] = dict()
        self.save["general info"]["title"] = self.title
        self.save["general info"]["version"] = self.version
        
        """ self.no_gui_nodes """
        self.save["required nodes path"] = dict()
        self.save["required nodes path"]["path"] = "no_gui_nodes"
        self.save["required nodes path"]["no gui nodes"] = list()
        for ind, node in enumerate(self.no_gui_nodes):
            tmp = dict()
            tmp["index"] = ind
            tmp["title"] = node.title
            tmp["module_name"] = node.path
            self.save["required nodes path"]["no gui nodes"].append(tmp)

        """ self.registered_nodes """
        self.save["scripts"] = list()
        flow = dict()
        flow["title"] = "doSth"
        flow["flow"] = dict()
        flow["flow"]["registered nodes"] = list()
        for gid, node in self.registered_nodes.items():
            tmp = dict()
            tmp["gid"] = gid
            tmp["title"] = node.__class__.title
            flow["flow"]["registered nodes"].append(tmp)

        """ self.arrows """
        flow["flow"]["arrows"] = list()
        for arrow in self.arrows:
            u, v = arrow[0], arrow[1]
            tmp = dict()
            tmp["from"] = u
            tmp["to"] = v
            tmp["at"] = self.locations[(u, v)]
            flow["flow"]["arrows"].append(tmp)
        self.save["scripts"].append(flow)
        
        with open("sample.json", "w") as outfile:
            json.dump(self.save, outfile)

    
    def load(self):
        self.reset()
        tmp_no_gui_nodes = [] # temp of self.no_gui_nodes
        with open('sample.json') as json_file:
            aia = json.load(json_file)
            
            """ general info """
            general_info = aia["general info"]
            self.title = general_info["title"]
            self.version = general_info["version"]
            os.environ["TITLE"] = self.title
            os.environ["VERSION"] = self.version

            """ self.no_gui_nodes """
            required_nodes_path = aia["required nodes path"]
            path = required_nodes_path["path"]
            auto_loading_path = os.path.join(os.path.dirname(__file__), path)
            no_gui_nodes = required_nodes_path["no gui nodes"]
            auto_loading_nodes = list()
            for ngn in no_gui_nodes:
                module_name = ngn["module_name"]
                if module_name not in auto_loading_nodes:
                    auto_loading_nodes.append(module_name)
                    aln, aln_nodes = module_name.split("/")
                    aln_path = os.path.join(auto_loading_path, aln)
                    sys.path.append(aln_path)
                    nodes_py = os.path.join(os.path.dirname(__file__), aln_path)
                    nodes_py = os.path.join(nodes_py, aln_nodes)
                    try:
                        module_name = os.path.basename(nodes_py).split(".py")[0]
                        tmp_no_gui_nodes += __import__(module_name).export_nodes
                    except:
                        continue
            tmp_no_gui_nodes_title = [node.title for node in tmp_no_gui_nodes]
            for ngn in no_gui_nodes:
                title = ngn["title"]
                index = tmp_no_gui_nodes_title.index(title)
                self.no_gui_nodes.append(tmp_no_gui_nodes[index])

            """ self.registered_nodes """
            scripts = aia["scripts"]
            flow = scripts[0]
            registered_nodes = flow["flow"]["registered nodes"]
            max_gid = -1
            for registered_node in registered_nodes:
                gid = registered_node["gid"]
                
                node_title = registered_node["title"]
                index = tmp_no_gui_nodes_title.index(node_title)
                new_node = tmp_no_gui_nodes[index]()
                new_node.global_id = gid
                self.registered_nodes[gid] = new_node
                if gid > max_gid:
                    max_gid = gid
                    new_node.update_ctr(max_gid)
            

            """ self.arrows """
            arrows = flow["flow"]["arrows"]
            for arrow in arrows:
                u = arrow["from"]
                v = arrow["to"]
                ind = arrow["at"]
                self.arrows.append([u, v])
                self.locations[(u, v)] = ind
                self.registered_nodes[v].nodeinputs[ind] = self.registered_nodes[u]

            self.updating_toposort()
            for ver in self.order:
                if self.registered_nodes[ver].num_inp > 0:
                    self.registered_nodes[ver].update_event()

            json_file.close()


class export_widgets:

    Coordinator = Coordinator