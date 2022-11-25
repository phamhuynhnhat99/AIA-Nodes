from .cell import Cell
from .cell_value import CellValue

from PIL import ImageTk

class CellOp(Cell):
    def __init__(self, canvas, num_inp=0, num_out=1, view = "", text = '', W = 50, H = 50):
        if num_inp >= 0:
            self.num_inp = num_inp
        else:
            self.num_inp = 0
        self.num_out = num_out

        center = (W, H)
        super().__init__(canvas=canvas, view=view,  W=W, H=H, text=text, center=center)
        self.text = text
        self.canvas = canvas
        self.celllineinputs = dict()

        self.cellvalueoutput_ = CellValue(canvas, r=10, center=(1.5*W, H))
        if num_inp == 0:
            self.cellvalueoutput_.value = self.get_output()
        self.celloutput_ = None
            
        self.cellvalueinputs = dict()
        self.cellinputs = dict()

        if self.num_inp > 0:
            space = int(H/(num_inp+1))
            for _ in range(self.num_inp):
                self.cellvalueinputs[_] = CellValue(canvas, r=10, center=(0.5*W, 0.5*H + (_+1)*space))
                
        IDs = [self.cellvalueoutput_.ID]
        for cellvalueinput in self.cellvalueinputs.values():
            IDs.append(cellvalueinput.ID)

        self.allIDs = self.allIDs + IDs
        self.bind_all_to_movement()
        self.bindtoclick()

    def bindtoclick(self):
        for _, cellvalueinput in self.cellvalueinputs.items():
            self.canvas.tag_bind(cellvalueinput.ID, '<1>', self.is_v_cell(_))
        self.canvas.tag_bind(self.cellvalueoutput_.ID, '<1>', self.is_u_cell())

    def is_v_cell(self, ind):
        return lambda event: self.b1_inputs(event, ind)
    
    def is_u_cell(self):
        return lambda event: self.b1_output(event)
    
    def b1_inputs(self, event, ind): # click v at position "ind"
        if ind in self.cellinputs.keys():
            del self.cellinputs[ind]
        if ind in self.celllineinputs.keys():
            self.canvas.delete(self.celllineinputs[ind].ID)
            del self.celllineinputs[ind]

        self.canvas.clickcount_v += 1
        self.canvas.IDc = ind
        self.canvas.v = self # v
        if self.canvas.clickcount_u == self.canvas.clickcount_v == 1:
            self.canvas.clickcount_u = 0
            self.canvas.clickcount_v = 0
            self.canvas.conectcells()
        elif self.canvas.clickcount_v == 2:
            self.canvas.clickcount_v = 0
            self.update()


    def b1_output(self, event): # click u at position "ind"
        self.canvas.clickcount_u += 1
        self.canvas.u = self # u

        if self.canvas.clickcount_u == self.canvas.clickcount_v == 1:
            self.canvas.clickcount_u = 0
            self.canvas.clickcount_v = 0
            self.canvas.conectcells()
        elif self.canvas.clickcount_u == 2:
            self.canvas.clickcount_u = 0


    def update(self):
        self.cellvalueoutput_.value = self.get_output()
        if self.view == "image":
            self.current_img = ImageTk.PhotoImage(self.cellvalueoutput_.value)
            self.canvas.itemconfig(self.ID, image=self.current_img)

        self.canvas.after(1000, self.update)