from tkinter import *
import json
from PIL import ImageTk,Image
from tkinter import filedialog
root = Tk()
root.title('Polymath Tech')
root.iconbitmap('C:/Users/23480/Desktop/Datascience/Tkinter/codemy/umbrella.ico')
# filename = filedialog.askopenfilename(initialdir="/Users/23480/Desktop/Datascience/Tkinter/codemy", title="select a file", filetypes=(("png files", "*.png"),("jpeg files", "*.jpg"),("all files", "*.*")))
#  mylabel= Label(root, text=filename).pack()
# img = ImageTk.PhotoImage(Image.open(filename))
# my_img_label = Label(image=img).pack()

def open():
    global img
    filename = filedialog.askopenfilename(initialdir="/Users/23480/Desktop/Datascience/Tkinter/codemy", title="select a file", filetypes=(("png files", "*.png"),("jpeg files", "*.jpg"),("all files", "*.*")))
    # mylabel= Label(root, text=filename).pack()
    img = ImageTk.PhotoImage(Image.open(filename))
    my_img_label = Label(image=img).pack()

my_btn = Button(root, text="choose a file", command=open).pack()
root.mainloop()