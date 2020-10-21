from tkinter import *

root = Tk()

root.title("Polymath Tech")
root.iconbitmap('C:/Users/DELL/Desktop/Tkinter/new_repo/codemy/umbrella.ico')
root.geometry("400x400")

class keyboard():
    def __init__(self, master):
        self.button = Button(master, text='Click Me!', command=self.clicker)
        self.button.pack(pady=20)

    def clicker(self):
        self.myLabel = Label(self.master, text='You clicked a button')
        self.myLabel.pack()

key = keyboard(root)


root.mainloop()