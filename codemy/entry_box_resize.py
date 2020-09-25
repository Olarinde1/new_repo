from tkinter import *

root = Tk()

root.title('Polymath Tech')
root.iconbitmap('C:/Users/DELL/Desktop/Tkinter/new_repo/codemy/umbrella.ico')
root.geometry("400x400")

def myClick():
    hello = "hello " + entry.get()
    myLabel = Label(root, text=hello)
    entry.delete(0, END)
    myLabel.pack(pady=10)
entry = Entry(root, width=20, font=('Helvetica', 30))
entry.pack(padx=10, pady=10)
myButton= Button(root, text='Enter your  Name', command=myClick)
myButton.pack(pady=10)
root.mainloop()