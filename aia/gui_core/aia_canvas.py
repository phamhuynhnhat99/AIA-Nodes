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
        self.xscrollbar_max, self.yscrollbar_max = 5000, 5000
        self.scrollbar_width = 20

        self.yscrollbar = tk.Scrollbar(master, orient = tk.VERTICAL, width=self.scrollbar_width)
        self.yscrollbar.pack(side = tk.RIGHT, fill = tk.Y)
 
        self.xscrollbar = tk.Scrollbar(master, orient = tk.HORIZONTAL, width=self.scrollbar_width)
        self.xscrollbar.pack(side = tk.BOTTOM, fill = tk.X)

        self.config(
            width=W, height=H,
            scrollregion=(0, 0, 5000, 5000),
            xscrollcommand = self.xscrollbar.set,
            yscrollcommand = self.yscrollbar.set,
            background='#b3aa99')
        
        self.xscrollbar.config(command = self.xview)
        self.yscrollbar.config(command = self.yview)

        # Root --- Arrow Key Detection
        master.bind("<Up>", self.arrow_detected("Up"))
        master.bind("<Left>", self.arrow_detected("Left"))
        master.bind("<Down>", self.arrow_detected("Down"))
        master.bind("<Right>", self.arrow_detected("Right"))


    def arrow_detected(self, type):
        def arrow_detected_lambda(event, type):
            step = 0.002
            scrollbar_x, scrollbar_y = (self.xscrollbar.get()[1] - 0.3202), (self.yscrollbar.get()[1] - 0.1802)
            if type == "Up":
                new_y = scrollbar_y - step if scrollbar_y - step >= 0.0 else 0.0
                self.yview_moveto(str(new_y))
            if type == "Left":
                new_x = scrollbar_x - step if scrollbar_x - step >= 0.0 else 0.0
                self.xview_moveto(str(new_x))
            if type == "Down":
                new_y = scrollbar_y + step if scrollbar_y + step <= 1.0 else 1.0
                self.yview_moveto(str(new_y))
            if type == "Right":
                new_x = scrollbar_x + step if scrollbar_x + step <= 1.0 else 1.0
                self.xview_moveto(str(new_x))
        return lambda event: arrow_detected_lambda(event, type=type)


    def get_scrollbar_delta(self):
        scrollbar_x = (self.xscrollbar.get()[1] - 0.3202) * self.xscrollbar_max
        scrollbar_y = (self.yscrollbar.get()[1] - 0.1802) * self.yscrollbar_max
        return scrollbar_x, scrollbar_y


    def conectcells(self): # self.u and self.v are definitely not None
        if self.u.global_id != self.v.global_id:
            self.v.cellinputs[self.IDc] = self.u
            self.line = CellLine(self, self.u, self.v) # create new line from u to v

        self.v.update()