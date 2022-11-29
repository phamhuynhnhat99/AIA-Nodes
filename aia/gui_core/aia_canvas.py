import tkinter as tk
from .cell_line import CellLine

class AIACanvas(tk.Canvas):

    def __init__(self, master, W = 1600, H = 900):
        super().__init__(master)

        self.u = None
        self.v = None
        self.clickcount_u = 0
        self.clickcount_v = 0
        self.IDc = None

        # Create Scrollbar
        self.xscrollbar_max = 5000
        self.yscrollbar_max = 5000
        self.scrollbar_width = 20

        self.yscrollbar = tk.Scrollbar(master, orient = tk.VERTICAL, width=self.scrollbar_width)
        self.yscrollbar.pack(side = tk.RIGHT, fill = tk.Y)
 
        self.xscrollbar = tk.Scrollbar(master, orient = tk.HORIZONTAL, width=self.scrollbar_width)
        self.xscrollbar.pack(side = tk.BOTTOM, fill = tk.X)

        self.config(
            width=W,
            height=H,
            scrollregion=(0, 0, 5000, 5000),
            xscrollcommand = self.xscrollbar.set,
            yscrollcommand = self.yscrollbar.set,
            background='#b3aa97')
        
        self.xscrollbar.config(command = self.xview)
        self.yscrollbar.config(command = self.yview)


    def get_scrollbar_delta(self):
        scrollbar_x = (self.xscrollbar.get()[1] - 0.3202) * self.xscrollbar_max
        scrollbar_y = (self.yscrollbar.get()[1] - 0.1802) * self.yscrollbar_max
        return scrollbar_x, scrollbar_y


    def conectcells(self): # self.u and self.v are definitely not None
        if self.u.global_id != self.v.global_id:
            self.v.cellinputs[self.IDc] = self.u
            self.line = CellLine(self, self.u, self.v) # create new line from u to v

        self.v.update()