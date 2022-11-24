import tkinter

from aia.gui_core.aia_canvas import AIACanvas

import os

from aia.NENV import init_node_env


def run():

    def update():
        aiacanvas.after_idle(update)

    os.environ['AIA_MODE'] = 'gui'
    init_node_env()

    from aia.main.gui_nodes.opencv.opencv_nodes import ReadImage, ReadImageClone, ShowImage

    root = tkinter.Tk()
    root.title('AIA-Nodes')
    aiacanvas = AIACanvas(root)

    cell = ReadImage(aiacanvas, num_inp=0, num_out=1, view = "button", W = 200, H = 50)
    cell = ReadImageClone(aiacanvas, num_inp=0, num_out=1, view = "button", W = 200, H = 50)

    cell = ShowImage(aiacanvas, num_inp=2, num_out=1, view = "image", W = 400, H = 300)

    aiacanvas.pack()

    root.after(20, update)
    root.mainloop()
    
    print("----------------------------------------")
    print("Good luck Have fun.")


if __name__ == '__main__':
    run()