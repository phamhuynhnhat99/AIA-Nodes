from aia.flow.flow import Flow

class Coordinator:

    def __init__(self):
        self.flow = Flow()
        self.auto_nodes = []
        self.arrows = []
        self.registered_nodes = dict()
        self.order = []


    def display_auto_nodes(self):
        print("-oOo-         All of nodes         -oOo-")
        for i, node in enumerate(self.auto_nodes):
            print("    Index:", i, "   ", node.title)

    
    def display_registered_nodes(self):
        for gid, node in self.registered_nodes.items():
            print("    id:", gid, "   ", node.__class__.title)


    def display_arrows(self):
        for id, arrow in enumerate(self.arrows):
            print("             ", arrow[0], '---->', arrow[1])

    
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
        if gid in self.registered_nodes.keys():
            if self.order is not None:
                genealogy_of_u = self.flow.sub_toposort_from(gid)
                for ver in genealogy_of_u:
                    self.registered_nodes[ver].update_event()


    def registering_a_new_node(self, node_index):
        if 0 <= node_index and node_index < len(self.auto_nodes):
            new_node = self.auto_nodes[node_index]()
            self.registered_nodes[new_node.global_id] = new_node
            self.registered_nodes[new_node.global_id].update_event()
            self.updating_toposort()
            

    def registering_a_new_arrow(self, u, v):
        if u in self.registered_nodes.keys() and v in self.registered_nodes.keys():
            if [u, v] not in self.arrows:
                self.arrows.append([u, v])
                self.registered_nodes[v].push_prev_nodes(self.registered_nodes[u])
                self.updating_toposort()
                self.updating_a_registered_node(v)


    def removing_a_registered_node(self, gid):
        if gid in self.registered_nodes.keys():
            genealogy_of_u = self.flow.sub_toposort_from(gid)
            
            sub_arrows = [arrow for arrow in self.arrows if gid in arrow]
            for arrow in sub_arrows:
                u = arrow[0]
                v = arrow[1]
                self.registered_nodes[v].remove_prev_node(self.registered_nodes[u])
                self.arrows.remove(arrow)

            del self.registered_nodes[gid]
            
            self.updating_toposort()
            for ver in genealogy_of_u:
                self.registered_nodes[ver].update_event()


    def removing_a_registered_arrow(self, u, v):
        if [u, v] in self.arrows:
            self.arrows.remove([u, v])
            self.registered_nodes[v].remove_prev_node(self.registered_nodes[u])
            self.updating_toposort()
            self.updating_a_registered_node(v)


    def updating_order(self):
        pass



class export_widgets:

    Coordinator = Coordinator