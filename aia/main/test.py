
from tkinter import *
 
root = Tk()
root.geometry("300x120")
root.title("Yolov5s")
 
def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    try:
        min_conf = float(INPUT)
    except:
        min_conf = None
    if min_conf:
        Output.delete("1.0", END)
        Output.insert(END, 'Correct')
        root.destroy()
        root.quit()
        # self.min_confidence = min_conf
    else:
        Output.delete("1.0", END)
        Output.insert(END, "This is not a real number\nInput again, please")
     
l = Label(text = "What is min confidence?")
inputtxt = Text(root, height = 1,
                width = 20,
                bg = "#ffffb3")

Display = Button(root, height = 1,
                 width = 10,
                 text ="Enter",
                 bg = "#856ff8",
                 command = lambda:Take_input())
 
Output = Text(root, height = 2,
              width = 40,
              bg = "#ff8080")
 
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
 
mainloop()