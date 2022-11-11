from tkinter import *

class FloatTextWidget():

    def __init__(self):
        self.float_text = 0.0
        self.title = "Input"


    def set_title(self, title):
        self.title = title


    def get_float_text(self):

        def Take_input():
            INPUT = inputtxt.get("1.0", "end-1c")
            try:
                float_text = float(INPUT)
            except:
                float_text = None
            if float_text:
                self.float_text = float_text
                root.destroy()
                root.quit()
            else:
                Output.delete("1.0", END)
                Output.insert(END, "This is not a real number\nInput again, please")

        root = Tk()
        root.title(self.title)
        root.resizable(False, False)
        root.geometry("300x120")

        l = Label(text = "Enter a real number")
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

        return self.float_text


class export_widgets:

    FloatTextWidget = FloatTextWidget

