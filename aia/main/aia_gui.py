import tkinter

from aia.gui_core.aia_canvas import AIACanvas

import os

from aia.NENV import init_node_env


def run():

    global cell

    os.environ['AIA_MODE'] = 'gui'
    init_node_env()

    from aia.main.gui_nodes.image.image_nodes import ReadImage, ReadImageClone, ShowImage, BlurImage

    root = tkinter.Tk()
    root.title('AIA-Nodes')
    aiacanvas = AIACanvas(root)

    cell = ReadImage(aiacanvas, num_inp=0, num_out=1, view = "button", W = 200, H = 50)
    cell = ReadImageClone(aiacanvas, num_inp=0, num_out=1, view = "button", W = 200, H = 50)
    cell = BlurImage(aiacanvas, num_inp=1, num_out=1, view="rectangle", W=200, H=50)
    cell = ShowImage(aiacanvas, num_inp=1, num_out=1, view = "image", W = 200, H = 300)
    cell = ShowImage(aiacanvas, num_inp=1, num_out=1, view = "image", W = 400, H = 500)
    cell = ShowImage(aiacanvas, num_inp=1, num_out=1, view = "image", W = 600, H = 700)

    aiacanvas.pack()
    root.mainloop()
    
    print("----------------------------------------")
    print("Good luck Have fun.")


if __name__ == '__main__':
    run()