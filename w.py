#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Set the geometry of frame
win.geometry("650x450")

#Define a function for Button Object
def quit_win():
   win.quit()
def destroy_win():
   win.destroy()

#Button for Quit Method
Button(win,text="Quit", command=quit_win, font=('Helvetica bold',20)).pack(pady=5)

#Button for Destroy Method
Button(win, text= "Destroy", command=destroy_win, font=('Helvetica bold',20)).pack(pady=5)
win.mainloop()