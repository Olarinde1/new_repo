from tkinter import *
def onClick():
    myLabel = Label(root, text='i clicked this button!', fg='red')
    myLabel.pack()


root = Tk()
myButton = Button(root, text='click here', padx=50, pady=5, command=onClick, fg='blue', bg='#000000')
myButton.pack()

root.mainloop()