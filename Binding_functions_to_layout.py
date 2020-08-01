from tkinter import *

root = Tk()

def printName(event):
    print('my name is Olarinde Alli')

button_1 = Button(root, text='click to print your name')
button_1.bind("<Button-1>", printName)
button_1.pack()

def leftClick(event):
    print('left click')

def midClick(event):
    print('middle click')

def rightClick(event):
    print('right click')

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", midClick)
frame.bind("<Button-3>", rightClick)

frame.pack()
root.mainloop()