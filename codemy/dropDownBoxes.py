from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
root = Tk()
root.title('Polymath Tech')
root.iconbitmap('C:/Users/23480/Desktop/Datascience/Tkinter/codemy/umbrella.ico')
root.geometry("400x400")

def show():
    label = Label(root, text=var.get()).pack()

options = [
    "Sunday",
    "Monday",
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
]
var = StringVar()
var.set(options[1])
drop = OptionMenu(root, var, *options)
drop.pack()
btn = Button(root, text='show selection', command=show).pack()

root.mainloop()
