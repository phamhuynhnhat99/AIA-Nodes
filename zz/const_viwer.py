from cell import Cell
from cell_value import CellValue
class ConstViwer(Cell):
    def __init__(self,canvas,text = ''):# CONTRUTOR DA CLASSE FILHA
        super().__init__(canvas = canvas,W=50,text= text) # construtor da classe PAI(Cell)
        self.line1 = None
        self.line2 = None
        self.text = text
        self.canvas = canvas
        self.output_ = CellValue(canvas,r=10,center=(125,50))
        #self.input_2 = CellValue(canvas,r=10,center=(75,65))
        self.input_1 = CellValue(canvas,r=10,center=(75,50))
        self.cellinput1 = None
        self.cellinput2 = None
        self.celloutput = None
        self.allIDs = self.allIDs + [self.output_.ID,self.input_1.ID]
        self.bind_all_to_movement()
        self.bindtoclick()
    def bindtoclick(self):
        self.canvas.tag_bind(self.input_1.ID,'<1>',self.b1_input1)
        #self.canvas.tag_bind(self.input_2.ID,'<1>',self.b1_input2)
        self.canvas.tag_bind(self.output_.ID,'<1>',self.b1_output)
        self.canvas.tag_bind(self.output_.ID,'<3>',self.debug)
    def b1_output(self,event):
        self.canvas.clickcount += 1
        self.canvas.outputcell = self
        if self.canvas.clickcount == 2: 
            self.canvas.clickcount = 0
            self.canvas.conectcells()
    def b1_input1(self,event):
        try :self.canvas.delete(self.line1.ID)
        except: None
        self.canvas.clickcount += 1
        self.canvas.IDc = 'input1'
        self.canvas.inputcell = self
        if self.canvas.clickcount == 2: 
            self.canvas.clickcount = 0
            self.canvas.conectcells()
    def b1_input2(self,event):
        try:self.canvas.delete(self.line2.ID)
        except: None
        self.canvas.clickcount += 1
        self.canvas.IDc = 'input2'
        self.canvas.inputcell = self
        if self.canvas.clickcount == 2: 
            self.canvas.clickcount = 0
            self.canvas.conectcells()
    def update(self):
        try:
            self.output_.value = self.cellinput1.output_.value
            self.canvas.itemconfigure(self.IDtext,text = str(self.output_.value))
        except:None
        self.canvas.after(50,self.update)
    def debug(self,event):
        print(self.output_.value)
        #print(self.cellinput1.output_.value)
    