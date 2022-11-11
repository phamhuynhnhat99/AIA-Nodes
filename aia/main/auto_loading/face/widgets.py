from tkinter import *

class MinConfidenceBoxWidget():

    def __init__(self):
        self.min_confidence = 0.0

    def get_min_confidence(self):

        def Take_input():
            INPUT = inputtxt.get("1.0", "end-1c")
            try:
                min_conf = float(INPUT)
            except:
                min_conf = None
            if min_conf:
                self.min_confidence = min_conf
                Output.delete("1.0", END)
                Output.insert(END, 'Correct')
                root.destroy()
                root.quit()
            else:
                Output.delete("1.0", END)
                Output.insert(END, "This is not a real number\nInput again, please")

        root = Tk()
        root.title('Yolov5s')
        root.resizable(False, False)
        root.geometry("300x120")

        l = Label(text = "What is min confidence?")
        inputtxt = Text(root, height = 1,
                        width = 20,
                        bg = "#ffffb3")

        Display = Button(root, height = 1,
                        width = 10,
                        text ="Enter",
                        bg = "#856ff8",
                        command = Take_input)
        
        Output = Text(root, height = 2,
                    width = 40,
                    bg = "#ff8080")
        
        l.pack()
        inputtxt.pack()
        Display.pack()
        Output.pack()
        
        root.mainloop()

        return self.min_confidence


class export_widgets:

    MinConfidenceBoxWidget = MinConfidenceBoxWidget

