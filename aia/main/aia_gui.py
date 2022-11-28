import tkinter

from aia.gui_core.aia_canvas import AIACanvas

import os

from aia.NENV import init_node_env


def run():

    global cell

    os.environ['AIA_MODE'] = 'gui'
    init_node_env()

    from aia.main.gui_nodes.image.image_nodes import ReadImage, ShowImage, BlurImage, RemoveBackground

    root = tkinter.Tk()
    root.title('AIA-Nodes')
    aiacanvas = AIACanvas(root)
    aiacanvas.configure(background='#b3aa97')

    cell = ReadImage(aiacanvas, num_inp=0, num_out=1, view = "button", W = 150, H = 60)
    cell = ReadImage(aiacanvas, num_inp=0, num_out=1, view = "button", W = 150, H = 60)

    cell = BlurImage(aiacanvas, num_inp=1, num_out=1, view="rectangle", W=200, H=50)

    cell = ShowImage(aiacanvas, num_inp=1, num_out=1, view = "image", W = 400, H = 300)
    cell = ShowImage(aiacanvas, num_inp=1, num_out=1, view = "image", W = 400, H = 300)
    
    cell = RemoveBackground(aiacanvas, num_inp=1, num_out=1, view = "button", W = 200, H = 50)

    aiacanvas.pack()
    root.mainloop()
    
    print("----------------------------------------")
    print("Good luck Have fun.")


if __name__ == '__main__':
    run()