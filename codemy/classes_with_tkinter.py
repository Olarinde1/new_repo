from tkinter import *

root = Tk()

root.title("Polymath Tech")
root.iconbitmap('C:/Users/DELL/Desktop/Tkinter/new_repo/codemy/umbrella.ico')
root.geometry("400x400")


class myApp():
    def __init__(self, master):
        self.myFrame = Frame(master)
        self.myFrame.pack()
        self.myButton = Button(master, text='Click Me!', command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print('Welocome to classes with tkinter')


app = myApp(root)

root.mainloop()