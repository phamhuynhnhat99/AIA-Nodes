class CellValue:
    def __init__(self,canvas,cell = None,center = (50,50),value = 0,r = 20,OUTLINE = 'white', LINEW = 3,FILL = 'red',):
        self.canvas = canvas
        self.value = value
        self.cell = cell
        self.center = center
        self.r = r
        self.create(OUTLINE,LINEW,FILL)
        self.update()
        self.signal = False

    def getpos(self,center = True):
        if center == True:
            self.cords = self.canvas.coords(self.ID)
            return (self.cords[0]+self.cords[2])/2 ,(self.cords[1]+self.cords[3])/2
        if center == False:
            return self.canvas.coords(self.ID)
    
    def create(self,OUTLINE,LINEW,FILL):
        self.ID = self.canvas.create_oval(
            (self.center[0]-self.r,self.center[1]-self.r),
            (self.center[0]+self.r,self.center[1]+self.r),
            outline = OUTLINE, width = LINEW , fill = FILL)
        self.canvas.tag_bind(self.ID,'<Enter>',self.enter)
        self.canvas.tag_bind(self.ID,'<Leave>',self.leave)
    
    def update(self):
        self.cords = self.canvas.coords(self.ID)
        self.center = (self.cords[0]+self.cords[2])/2 ,(self.cords[1]+self.cords[3])/2
        #if self.signal == False : self.canvas.itemconfigure(self.ID,fill = '#9F4347')
        #if self.signal == True : self.canvas.itemconfigure(self.ID,fill = '#B91428')
        try:
            if self.signal == False : self.canvas.itemconfigure(self.ID,fill = 'red')
            if self.signal == True : self.canvas.itemconfigure(self.ID,fill = '#B91428')
        except:None
        self.canvas.after(10,self.update)
    
    def enter(self,event):
        self.signal = True
    def leave(self,event):
        self.signal = False
        
    
        