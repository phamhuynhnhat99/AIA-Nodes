import tkinter as tk
 
 
class MainWindow:
    def __init__(self, master):
        self.master = master
 
        self.frame = tk.Frame(self.master)
        self.frame.pack()
 
        self.label = tk.Label(self.frame, text = "ScrollBar Demo")
        self.label.pack()
 
        self.yscrollbar = tk.Scrollbar(self.frame, orient = tk.VERTICAL)
        self.yscrollbar.pack(side = tk.RIGHT, fill = tk.Y)
 
        self.xscrollbar = tk.Scrollbar(self.frame, orient = tk.HORIZONTAL)
        self.xscrollbar.pack(side = tk.BOTTOM, fill = tk.X)
 
        self.canvas = tk.Canvas(self.frame, width = 300, height = 300, scrollregion = (0, 0, 500, 500),
                                xscrollcommand = self.xscrollbar.set, yscrollcommand = self.yscrollbar.set,
                                bg = "white")
        self.canvas.pack()
 
        self.yscrollbar.config(command = self.canvas.yview)
        self.xscrollbar.config(command = self.canvas.xview)
         
 
root = tk.Tk()
window = MainWindow(root)
root.mainloop()