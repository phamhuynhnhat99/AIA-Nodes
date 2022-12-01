import tkinter as tk
from tkinter import ttk

from aia.gui_core.aia_canvas import AIACanvas, MenuCanvas

import os

from aia.NENV import init_node_env, import_widgets
utils = import_widgets(__file__, "gui_utils.py")

global node

def run():

    def node_clicked(_):
        def node_clicked_lambda(_):
            cell = gui_utils.gui_nodes[_](aiacanvas)
        return lambda: node_clicked_lambda(_)


    os.environ['AIA_MODE'] = 'gui'
    init_node_env()

    gui_utils = utils.GUI_utils()
    gui_utils.auto_loading()

    root = tk.Tk()
    root.geometry("1643x922")
    root.title('AIA-Nodes')
    root.resizable(True, True)

    aiacanvas = AIACanvas(root)

    menu = MenuCanvas(root)

    for _, gui_node in enumerate(gui_utils.gui_nodes):
        button = tk.Button(menu, text = gui_node.title, command = node_clicked(_), anchor = "center")
        button.configure(bd = 2, width = 15, activebackground = "#ff00ee", relief = tk.FLAT)
        button.grid()

        ID = menu.create_window(
            100,
            50+_*50,
            anchor="center",
            window=button)

    root.mainloop()
    
    print("----------------------------------------")
    print("Good luck Have fun.")


if __name__ == '__main__':
    run()