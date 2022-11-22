import tkinter as tk
from cell_line import CellLine
# --- --- --- --- ---
class MathCanvas(tk.Canvas):
    def __init__(self,master,W = 1600, H = 900): # construtor da classe FILHO(MathCanvas)
        super().__init__(master,width = W, height = H) # construtor da classe PAI(tk.Canvas)
        self.inputcell = None
        self.outputcell = None
        self.clickcount = 0
        self.IDc = None
    def conectcells(self):
        if self.IDc == 'input1':
            #self.inputcell.input_1.value = self.outputcell.output_.value
            self.inputcell.cellinput1 = self.outputcell
        if self.IDc == 'input2':
            #self.inputcell.input_2.value = self.outputcell.output_.value
            self.inputcell.cellinput2 = self.outputcell
        self.line = CellLine(self,self.outputcell,self.inputcell)
        self.inputcell.update()