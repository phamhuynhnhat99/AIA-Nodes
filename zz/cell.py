class Cell:
    def __init__(self,canvas,type_ = None,W=100,H=50,outline = 'white', linew = 3,fill = 'grey', center = (100,50), text = ''):
        self.canvas = canvas
        self.W = W ; self.H = H
        self.OUTLINE = outline; self.LINEW = linew; self.FILL = 'grey';self.text = text 
        self.center = center
        self.auxlist = []
        
        self.create()
    def create(self):
        self.ID = self.canvas.create_rectangle(
            (self.center[0]-self.W*0.5,self.center[1]-self.H*0.5),
            (self.center[0]+self.W*0.5,self.center[1]+self.H*0.5),
            outline = self.OUTLINE , width = self.LINEW,fill = self.FILL)
        if self.text == 'MOD': self.IDtext = self.canvas.create_text(self.center, text = '')
        else : self.IDtext = self.canvas.create_text(self.center, text = self.text)
        #self.IDtext = self.canvas.create_text(self.center, text = self.text)
        self.allIDs = [self.ID,self.IDtext]
        self.auxlist = [self.ID,self.IDtext]
    
    def getpos(self,center = True):
        if center == True:
            self.cords = self.canvas.coords(self.ID)
            return (self.cords[0]+self.cords[2])/2 ,(self.cords[1]+self.cords[3])/2
        if center == False:
            return self.canvas.coords(self.ID)
    def bind_all_to_movement(self):
        for id_ in self.auxlist :
            self.canvas.tag_bind(id_,'<B1-Motion>',self.mouse_mov)
    
    def mouse_mov(self,event):
        self.x,self.y = self.getpos()
        self.xmove = event.x - self.x 
        self.ymove = event.y - self.y
        for id_ in self.allIDs:
            self.canvas.move(id_,self.xmove,self.ymove)    
    