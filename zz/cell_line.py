class CellLine():
    def __init__(self,canvas,firstcell,secondcell):
        self.canvas = canvas
        self.firstcell = firstcell # output
        self.secondcell = secondcell
        self.IDc = self.canvas.IDc
        self.create()
        self.update()
        

    def create(self):
        self.firstcell.line = self
        self.x1,self.y1 = self.firstcell.output_.center
        if self.canvas.IDc == 'input1':
            self.x2,self.y2 = self.secondcell.input_1.center
            self.secondcell.line1 = self
        if self.canvas.IDc == 'input2':
            self.x2,self.y2 = self.secondcell.input_2.center
            self.secondcell.line2 = self
        self.ID = self.canvas.create_line(self.x1,self.y1,self.x2,self.y2,dash=(1, 2))
        self.canvas.tag_lower(self.ID)
        
    
    def update(self):
        self.x1,self.y1 = self.firstcell.output_.center
        if self.IDc == 'input1': self.x2,self.y2 = self.secondcell.input_1.center
        if self.IDc == 'input2': self.x2,self.y2 = self.secondcell.input_2.center
        self.canvas.coords(self.ID,self.x1,self.y1,self.x2,self.y2)
        self.canvas.after(10,self.update)