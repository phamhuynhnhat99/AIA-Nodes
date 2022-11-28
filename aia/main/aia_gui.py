import tkinter

from aia.gui_core.aia_canvas import AIACanvas

import os

from aia.NENV import init_node_env, import_widgets
utils = import_widgets(__file__, "gui_utils.py")

global node

def run():

    def node_clicked(_):
        return lambda: create_new_node(_)

    def create_new_node(_):
        cell = gui_utils.gui_nodes[_](aiacanvas)


    os.environ['AIA_MODE'] = 'gui'
    init_node_env()

    gui_utils = utils.GUI_utils()
    gui_utils.auto_loading()

    root = tkinter.Tk()
    root.title('AIA-Nodes')
    aiacanvas = AIACanvas(root)

    
    for _, gui_node in enumerate(gui_utils.gui_nodes):
        node = gui_node
        button = tkinter.Button(aiacanvas, text = gui_node.title, command = node_clicked(_), anchor = "center")
        button.configure(width = 15, activebackground = "#ff00ee", relief = tkinter.FLAT)
        button.pack(side = tkinter.TOP)

        ID = aiacanvas.create_window(
            100,
            50+_*50,
            anchor="center",
            window=button)

    aiacanvas.pack()
    root.mainloop()
    
    print("----------------------------------------")
    print("Good luck Have fun.")


if __name__ == '__main__':
    run()