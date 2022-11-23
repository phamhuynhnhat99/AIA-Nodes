import tkinter

from aia.gui_core.aia_canvas import AIACanvas

import os

from aia.NENV import init_node_env

def run():
    os.environ['AIA_MODE'] = 'gui'
    init_node_env()

    from aia.main.gui_nodes.opencv.opencv_nodes import ReadImage, ShowImage

    root = tkinter.Tk()
    root.title('AIA-Nodes')
    aiacanvas = AIACanvas(root)

    # cell = ReadImage(aiacanvas, num_inp=0, num_out=1, view = "button", W = 250, H = 150)

    cell = ShowImage(aiacanvas, num_inp=1, num_out=1, view = "image", W = 400, H = 300)

    aiacanvas.pack()
    root.mainloop()
    
    print("----------------------------------------")
    print("Good luck Have fun.")


if __name__ == '__main__':
    run()