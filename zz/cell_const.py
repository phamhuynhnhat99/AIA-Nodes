from cell import Cell
from cell_value import CellValue
class CellConst(Cell):
    def __init__(self,canvas,const = 0):# CONTRUTOR DA CLASSE FILHA
        super().__init__(canvas = canvas,W=50,text=str(const)) # construtor da classe PAI(Cell)
        self.output_ = CellValue(canvas,value = const,r=10,center=(125,50))
        self.allIDs = self.allIDs + [self.output_.ID]
        self.bind_all_to_movement()
        self.bindtoclick()
    def getvalue(self):
        return self.output_.value
    def bindtoclick(self):
        self.canvas.tag_bind(self.output_.ID,'<1>',self.b1_output)
    def b1_output(self,event):
        self.canvas.clickcount += 1
        self.canvas.outputcell = self
        if self.canvas.clickcount == 2:
            self.canvas.clickcount = 0
            self.canvas.conectcells()
    def update(self):
        self.canvas.after(10,self.update)

        
        
