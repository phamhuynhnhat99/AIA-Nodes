import tkinter as tk
from .cell_line import CellLine

class AIACanvas(tk.Canvas):

    def __init__(self, master, W = 1600, H = 900):
        super().__init__(master, width = W, height = H)

        self.arrows = list()

        self.old_u_id = None

        self.u = None
        self.v = None
        self.clickcount = 0
        self.IDc = None

    def conectcells(self):
        if self.u and self.v:

            arrow = [self.u.global_id, self.v.global_id, self.IDc]
            old_arrow = [self.old_u_id, self.v.global_id, self.IDc]

            if self.IDc not in self.v.cellinputs.keys():      
                self.arrows.append(arrow)
                self.v.cellinputs[self.IDc] = self.u
                self.line = CellLine(self, self.u, self.v)
            else:
                del self.v.cellinputs[self.IDc]
                if self.IDc in self.v.celllineinputs.keys():
                    self.delete(self.v.celllineinputs[self.IDc].ID)
                    del self.v.celllineinputs[self.IDc]

                if self.old_u_id is not None:
                    self.arrows.remove(old_arrow)
                    if self.old_u_id != self.u.global_id:
                        self.arrows.append(arrow)
                        self.v.cellinputs[self.IDc] = self.u
                        self.line = CellLine(self, self.u, self.v)
                else:
                    self.arrows.remove(arrow)
                    
            self.v.update()

        self.reset()

    def update_old_u(self, v, idc):
        for arrow in self.arrows:
            if arrow[1] == v.global_id and arrow[2] == idc:
                self.old_u_id = arrow[0]
                break

            
    def reset(self):
        self.old_u_id = None
        self.u = None
        self.v = None
        self.clickcount = 0
        self.IDc = None