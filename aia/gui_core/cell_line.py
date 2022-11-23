class CellLine():

    def __init__(self, canvas, u_cell, v_cell):
        self.canvas = canvas
        self.u_cell = u_cell # u
        self.v_cell = v_cell # v
        self.IDc = self.canvas.IDc
        self.create()
        self.update()
        

    def create(self):
        # self.u_cell.line = self
        self.x1, self.y1 = self.u_cell.cellvalueoutput_.center
        self.x2, self.y2 = self.v_cell.cellvalueinputs[self.IDc].center
        self.v_cell.celllineinputs[self.IDc] = self

        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
        self.ID = self.canvas.create_line(x1, y1, x2, y2, dash=(1, 2))
        self.canvas.tag_lower(self.ID)
        
    
    def update(self):
        self.x1, self.y1 = self.u_cell.cellvalueoutput_.center
        self.x2, self.y2 = self.v_cell.cellvalueinputs[self.IDc].center

        self.canvas.coords(self.ID, self.x1, self.y1, self.x2, self.y2)
        self.canvas.after(10, self.update)