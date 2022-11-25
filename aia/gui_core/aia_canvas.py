import tkinter as tk
from .cell_line import CellLine

class AIACanvas(tk.Canvas):

    def __init__(self, master, W = 1600, H = 900):
        super().__init__(master, width = W, height = H)

        self.u = None
        self.v = None
        self.clickcount_u = 0
        self.clickcount_v = 0
        self.IDc = None


    def conectcells(self): # self.u and self.v are definitely not None
        if self.u.global_id != self.v.global_id:
            self.v.cellinputs[self.IDc] = self.u
            self.line = CellLine(self, self.u, self.v) # create new line from u to v

        self.v.update()