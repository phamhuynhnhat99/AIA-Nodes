import tkinter as tk
from .cell_line import CellLine

class AIACanvas(tk.Canvas):

    def __init__(self, master, W = 1600, H = 900):
        super().__init__(master, width = W, height = H)

        self.arrows = []

        self.u = None
        self.v = None
        self.clickcount = 0
        self.IDc = None

    def conectcells(self):
        if self.u and self.v:
            arrow = [self.u.global_id, self.v.global_id]
            if arrow not in self.arrows:
                self.arrows.append(arrow)
                self.v.cellinputs[self.IDc] = self.u
                self.line = CellLine(self, self.u, self.v)
            else:
                self.arrows.remove(arrow)
                self.v.cellinputs[self.IDc] = None
                try:
                    self.delete(self.v.celllineinputs[self.IDc].ID)
                except:
                    None
                    
            self.v.update()
            self.reset()

    def reset(self):
        self.u = None
        self.v = None
        self.clickcount = 0
        self.IDc = None