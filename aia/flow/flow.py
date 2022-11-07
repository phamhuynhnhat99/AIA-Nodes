class Flow:

    def __init__(self):
        self.vertices = list()
        self.arrows = list()


    def constructor(self, vertices, arrows):

        self.decode_vertices = vertices
        self.vertices = [_ for _ in range(len(vertices))]
        
        self.arrows = []
        for arrow in arrows:
            u = vertices.index(arrow[0])
            v = vertices.index(arrow[1])
            self.arrows.append([u, v])
        self.m = len(self.arrows)
    

    def toposort(self):

        if not self.vertices or not self.arrows:
            return list(), []
        
        num_prev = [0] * len(self.vertices)
        num_next = [0] * len(self.vertices)

        head = [-1] * len(self.vertices)
        before = [None] * self.m
        adj = [None] * self.m

        for i, ar in enumerate(self.arrows):
            u, v = ar[0], ar[1]
            num_next[u] += 1
            num_prev[v] += 1
            adj[i] = v
            before[i] = head[u]
            head[u] = i

        end_vertices = [u for u in self.vertices if num_next[u] == 0]
        
        topo_queue = []
        for ver in self.vertices:
            if num_prev[ver] == 0:
                topo_queue.append(ver)
        
        toposort = []
        b_ind, e_ind = 0, 0
        while b_ind <= e_ind:
            if len(topo_queue) > 0:
                u = topo_queue[0]
                topo_queue = topo_queue[1:]
                e_ind += 1
                toposort.append(u)
                pos = head[u]
                while pos != -1:
                    v = adj[pos]
                    num_prev[v] -= 1
                    if num_prev[v] == 0:
                        topo_queue.append(v)
                    pos = before[pos]
                b_ind += 1
            else:
                break
        
        if e_ind < len(self.vertices):
            toposort = list()
            end_vertices = list()

        # decode
        decode_toposort = [self.decode_vertices[_] for _ in toposort]
        decode_end_vertices = [self.decode_vertices[_] for _ in end_vertices]
        return decode_toposort, decode_end_vertices
        