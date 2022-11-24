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

        if (self.u is not None) and (self.v is not None) and (self.u.global_id != self.v.global_id):

            arrow = [self.u.global_id, self.v.global_id, self.IDc]
            old_arrow = [self.old_u_id, self.v.global_id, self.IDc]

            if self.IDc not in self.v.cellinputs.keys(): # v.cellinputs at IDc is None
                self.arrows.append(arrow)
                self.v.cellinputs[self.IDc] = self.u
                self.line = CellLine(self, self.u, self.v) # create new line from u to v

            else: # v.cellinputs at IDc is not None
                del self.v.cellinputs[self.IDc] # remove it

                if self.IDc in self.v.celllineinputs.keys():
                    self.delete(self.v.celllineinputs[self.IDc].ID) # remove its line
                    del self.v.celllineinputs[self.IDc]

                if self.old_u_id is not None:
                    self.arrows.remove(old_arrow)
                    if self.old_u_id != self.u.global_id:
                        self.arrows.append(arrow)
                        self.v.cellinputs[self.IDc] = self.u
                        self.line = CellLine(self, self.u, self.v) # create new line from u to v
                else:
                    self.arrows.remove(arrow)
                    
            self.v.update()

        self.reset()
        print(self.arrows)

            
    def reset(self):
        self.old_u_id = None
        self.u = None
        self.v = None
        self.clickcount = 0
        self.IDc = None