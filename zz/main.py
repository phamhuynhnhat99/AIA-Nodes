import tkinter
from mathcanvas import MathCanvas
from cell_const import CellConst
from cell_op import CellOp
from cell_op2 import CellOp2
from const_viwer import ConstViwer

root = tkinter.Tk()
mathcanvas = MathCanvas(root)
#cell = CellOp(mathcanvas,text='MOD',W = 70)
cell = CellOp(mathcanvas,text='SUB')
cell = CellOp(mathcanvas,text='DIV')
cell = CellOp2(mathcanvas,text='SQRT')
cell = CellConst(mathcanvas,const=10)
cell = CellConst(mathcanvas,const=20)
cell = CellConst(mathcanvas,const=10)
cell = CellConst(mathcanvas,const=20)
cell = ConstViwer(mathcanvas)

mathcanvas.pack()
root.mainloop()


