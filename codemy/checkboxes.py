from tkinter import *

import json
from PIL import ImageTk,Image
from tkinter import filedialog
root = Tk()
root.title('Polymath Tech')
root.iconbitmap('C:/Users/23480/Desktop/Datascience/Tkinter/codemy/umbrella.ico')
root.geometry("400x400")

def show():
    Label(root, text=var.get()).pack()

var = StringVar()

checkbox1 = Checkbutton(root, text='check this box', variable=var, onvalue='welcome', offvalue='goodbye')
checkbox1.deselect()
checkbox1.pack()

btn = Button(root, text='show selection', command=show).pack()


root.mainloop()