from tkinter import *

import json
from PIL import ImageTk,Image
from tkinter import filedialog
root = Tk()
root.title('Polymath Tech')
root.iconbitmap('C:/Users/23480/Desktop/Datascience/Tkinter/codemy/umbrella.ico')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=400)
vertical.pack()

def slide():
    label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + 'x' + str(vertical.get()))

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()


my_btn = Button(root, text='click me!', command=slide).pack()
root.mainloop()