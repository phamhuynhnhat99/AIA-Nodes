from tkinter import LAST as tk_arrow

class CellLine():

    def __init__(self, canvas, u_cell, v_cell):
        self.canvas = canvas
        self.u_cell = u_cell # u
        self.v_cell = v_cell # v
        self.IDc = self.canvas.IDc
        self.create()
        self.update()
        

    def create(self):
        self.u_cell.line = self

        self.x1, self.y1 = self.u_cell.cellvalueoutput_.center
        self.x2, self.y2 = self.v_cell.cellvalueinputs[self.canvas.IDc].center
        
        self.v_cell.celllineinputs[self.canvas.IDc] = self

        self.ID = self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, dash=(16, 9), fill="blue") #, arrow=tk_arrow)
        self.canvas.tag_lower(self.ID)
        
    
    def update(self):
        self.x1, self.y1 = self.u_cell.cellvalueoutput_.center
        if self.IDc in self.v_cell.cellvalueinputs.keys():
            self.x2, self.y2 = self.v_cell.cellvalueinputs[self.IDc].center

        self.canvas.coords(self.ID, self.x1, self.y1, self.x2, self.y2)
        self.canvas.after(10, self.update)