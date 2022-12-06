import tkinter as tk

def but_ex_1():
    print("Will it be destroyed?")
    root.destroy()
    
root = tk.Tk()
tk.Label(root, text="This is a window.").pack()
tk.Button(root, text="OK, go", command=but_ex_1).pack()
root.mainloop()

print("It did/not???")