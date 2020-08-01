from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Polymath Tech')
root.iconbitmap('C:/Users/23480/Desktop/Datascience/Tkinter/codemy/umbrella.ico')

def open():
    global my_img
    top = Toplevel()
    top.title('Second window')
    my_img = ImageTk.PhotoImage(Image.open("C:/Users/23480/OneDrive/Pictures/Screenshots/# 1 coursera.jpg"))
    Label(top, image=my_img).pack()
    Button(top, text='close window', command=top.destroy).pack()

Button(root, text='click to open second window', command=open).pack()
root.mainloop()


