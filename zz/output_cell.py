class OutputCell:
    def __init__(self,canvas,cell = None,center = (50,50),value = 0,r = 20):
        self.canvas = canvas
        self.value = value
        self.cell = cell
        self.center = center
        self.r = r
        self.ID = canvas.create_oval(
            (self.center[0]-self.r,self.center[1]-self.r),
            (self.center[0]+self.r,self.center[1]+self.r))
    
    def getpos(self,center = True):
        if center == True:
            self.cords = self.canvas.coords(self.ID)
            return (self.cords[0]+self.cords[2])/2 ,(self.cords[1]+self.cords[3])/2
        if center == False:
            return self.canvas.coords(self.ID)