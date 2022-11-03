class Flow:

    def __init__(self):
        self.vertices = list()
        self.arrows = list()


    def constructor(self, vertices, arrows):
        self.vertices = vertices
        self.n = max(self.vertices)
        self.arrows = arrows
        self.m = len(self.arrows)
    

    def toposort(self):

        if not self.vertices or not self.arrows:
            return list()
        
        scv = [0] * (self.n+1)
        head = [-1] * (self.n+1)
        before = [None] * self.m
        adj = [None] * self.m

        for i, ar in enumerate(self.arrows):
            u, v = ar[0], ar[1]
            scv[v] += 1
            adj[i] = v
            before[i] = head[u]
            head[u] = i
        
        topo_queue = []
        for ver in self.vertices:
            if scv[ver] == 0:
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
                    scv[v] -= 1
                    if scv[v] == 0:
                        topo_queue.append(v)
                    pos = before[pos]
                b_ind += 1
            else:
                break
        
        return toposort
        