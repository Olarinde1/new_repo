from tkinter import *


class MyClass():
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text='print class', command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text='QUIT', command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print('This works successfully!')


root = Tk()
myObject = MyClass(root)
root.mainloop()