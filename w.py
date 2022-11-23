# import tkinter as tk

# class MainWindow(tk.Frame):
#     counter = 0
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#         self.button = tk.Button(self, text="Create new window", 
#                                 command=self.create_window)
#         self.button.pack(side="top")

#     def create_window(self):
#         self.counter += 1
#         t = tk.Toplevel(self)
#         t.wm_title("Window #%s" % self.counter)
#         l = tk.Label(t, text="This is window #%s" % self.counter)
#         l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

# if __name__ == "__main__":
#     root = tk.Tk()
#     main = MainWindow(root)
#     main.pack(side="top", fill="both", expand=True)
#     root.mainloop()

from tkinter import *
from PIL import Image, ImageTk

#----------------------------------------------------------------------

class MainWindow():

    #----------------
    
    def __init__(self, main):
        
        # canvas for image
        self.canvas = Canvas(main, width=1600, height=900)
        self.canvas.grid(row=0, column=0)
        
        # images
        self.my_images = []
        img = Image.open("/home/aia/Nhat/AIA-Nodes/aia.jpg")
        w, h = img.size
        scale = 400 / (w if w > h else h)
        new_size = (int(scale * w), int(scale * h))
        img = ImageTk.PhotoImage(img.resize(new_size))
        self.my_images.append(img)

        img = Image.open("/home/aia/Nhat/AIA-Nodes/test_rb.png")
        w, h = img.size
        scale = 400 / (w if w > h else h)
        new_size = (int(scale * w), int(scale * h))
        img = ImageTk.PhotoImage(img.resize(new_size))
        self.my_images.append(img)

        img = Image.open("/home/aia/Nhat/AIA-Nodes/Test_1.jpg")
        w, h = img.size
        scale = 400 / (w if w > h else h)
        new_w, new_h = int(scale * w), int(scale * h)
        new_size = (new_w, new_h)
        img = ImageTk.PhotoImage(img.resize(new_size))
        self.my_images.append(img)


        self.my_image_number = 0
        
        # set first image on canvas
        self.image_on_canvas = self.canvas.create_image(400, 400, anchor='nw', image=self.my_images[self.my_image_number])
        self.IDtext = self.canvas.create_text((400, 400), text = "Show Image")
        cords = self.canvas.coords(self.image_on_canvas)
        print(self.canvas.bbox(self.image_on_canvas))
        
        # button to change image
        self.button = Button(main, text="Change", command=self.onButton)
        self.button.grid(row=1, column=0)
        
    #----------------

    def onButton(self):
        
        # next image
        self.my_image_number += 1

        # return to first image
        if self.my_image_number == len(self.my_images):
            self.my_image_number = 0

        # change image
        self.canvas.itemconfig(self.image_on_canvas, image=self.my_images[self.my_image_number])

#----------------------------------------------------------------------

root = Tk()
MainWindow(root)
root.mainloop()