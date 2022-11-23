class CellCtr:
    """
    A simple ascending integer ID counter.
    """

    def __init__(self):
        self.ctr = -1

    def increasing(self):
        self.ctr += 1
        return self.ctr


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Cell:

    _global_id_ctr = CellCtr()

    def __init__(self, canvas, view = None, W=100, H=50, outline = 'white', linew = 3, fill = 'grey', center = (100, 50), text = ''):

        self.global_id = self._global_id_ctr.increasing()

        self.canvas = canvas
        self.view = view
        self.W = W
        self.H = H
        self.OUTLINE = outline
        self.LINEW = linew
        self.FILL = 'grey'
        self.text = text 
        self.center = center
        self.auxlist = []
        self.need_center = True
        self.create()   


    def create(self):
        if self.view == "button":
            self.ID = self.canvas.create_rectangle(
                (self.center[0]-self.W*0.5, self.center[1]-self.H*0.5),
                (self.center[0]+self.W*0.5, self.center[1]+self.H*0.5),
                outline = self.OUTLINE,
                width = self.LINEW,
                fill = self.FILL)
            self.need_center = True
        else:
            #Load an image in the script
            self.img = Image.open("/home/aia/Nhat/AIA-Nodes/test.png")
            w, h = self.img.size
            scale = self.W / (w if w > h else h)
            new_w, new_h = int(scale * w), int(scale * h)
            new_size = (new_w, new_h)
            self.img = ImageTk.PhotoImage(self.img.resize(new_size))
            
            self.ID = self.canvas.create_image(
                self.center[0],
                self.center[1],
                anchor="center",
                image = self.img)
            self.need_center = False

        northern = (self.center[0], self.center[1]-self.W//2)
        self.IDtext = self.canvas.create_text(northern, text = self.text)
        self.allIDs = [self.ID, self.IDtext]
        self.auxlist = [self.ID, self.IDtext]
    

    def getpos(self):
        if self.need_center == True:
            self.cords = self.canvas.coords(self.ID)
            return (self.cords[0]+self.cords[2])/2 ,(self.cords[1]+self.cords[3])/2
        
        return self.canvas.coords(self.ID)


    def bind_all_to_movement(self):
        for id_ in self.auxlist:
            self.canvas.tag_bind(id_, '<B1-Motion>', self.mouse_mov)
    

    def mouse_mov(self, event):
        self.x, self.y = self.getpos()
        self.xmove = event.x - self.x
        self.ymove = event.y - self.y
        for id_ in self.allIDs:
            self.canvas.move(id_, self.xmove, self.ymove)    
    