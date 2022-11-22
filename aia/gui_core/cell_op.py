from .cell import Cell
from .cell_value import CellValue
import tkinter as tk

class CellOp(Cell):
    def __init__(self, canvas, num_inp=0, num_out=1, text = 'CellOp', W = 50, H = 50):
        if num_inp >= 0:
            self.num_inp = num_inp
        else:
            self.num_inp = 0
        self.num_out = num_out

        center = (W, H)
        super().__init__(canvas=canvas, W=W, H=H, text=text, center=center)
        self.text = text
        self.canvas = canvas
        self.celllineinputs = dict()

        self.cellvalueoutput_ = CellValue(canvas, r=10, center=(1.5*W, H))
        self.celloutput_ = None

        self.cellvalueinputs = dict()
        self.cellinputs = dict()

        if self.num_inp > 0:
            space = int(H/(num_inp+1))
            for _ in range(self.num_inp):
                new_cellvalue = CellValue(canvas, r=10, center=(0.5*W, 0.5*H + (_+1)*space))
                self.cellvalueinputs[_] = new_cellvalue
                self.cellinputs[_] = None

        IDs = [self.cellvalueoutput_.ID]
        for cellvalueinput in self.cellvalueinputs.values():
            IDs.append(cellvalueinput.ID)

        self.allIDs = self.allIDs + IDs
        self.bind_all_to_movement()
        self.bindtoclick()

    def bindtoclick(self):
        for _, cellvalueinput in self.cellvalueinputs.items():
            self.canvas.tag_bind(cellvalueinput.ID, '<1>', self.b1_inputs_lambda(_))
        self.canvas.tag_bind(self.cellvalueoutput_.ID, '<1>', self.b1_output_lambda())

    def b1_inputs_lambda(self, ind):
        return lambda event: self.b1_inputs(event, ind)
    
    def b1_output_lambda(self):
        return lambda event: self.b1_output(event)
    
    def b1_inputs(self, event, ind):
        try:
            self.canvas.delete(self.celllineinputs[ind].ID) # remove old arrow
        except:
            None
        self.canvas.clickcount += 1
        self.canvas.IDc = ind
        self.canvas.v = self # v
        if self.canvas.clickcount == 2: # two vertices have been selected
            self.canvas.clickcount = 0
            if self.canvas.u != self: # u != v
                self.canvas.conectcells()

    def b1_output(self, event):
        self.canvas.clickcount += 1
        self.canvas.u = self # u
        if self.canvas.clickcount == 2: # two vertices have been selected
            self.canvas.clickcount = 0
            if self.canvas.v != self: # v != u
                self.canvas.conectcells()

    def update(self):
        try:
            self.cellvalueoutput_.value = self.get_output()
        except:
            None
        self.canvas.after(50, self.update)