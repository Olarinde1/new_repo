from tkinter import *

root = Tk() #creates a blank window
mylabel = Label(root, text='hello world!', bg='green', fg='white') # displaying a text on the root window
mylabel.pack(side=LEFT, fill=Y)  # packing the text in the window
mylabel1 = Label(root, text='this is the second label', bg='blue', fg='cyan')
mylabel1.pack(fill=X)
name = Label(root, text='name: ')
password = Label(root, text='password: ')
name_entry = Entry(root)
pass_entry = Entry(root)

name.grid(row=0)
password.grid(row=1)

name_entry.grid(row=0, column=1)
pass_entry.grid(row=1, column=1)

topframe = Frame(root)
topframe.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

botton1 = Button(topframe, text='Button 1', fg="red")
botton2 = Button(topframe, text='Button 2', fg="blue")
botton3 = Button(topframe, text='Button 3', fg="green")
botton4 = Button(bottomframe, text='Button 4', fg="purple")

botton1.pack(side=LEFT)
botton2.pack(side=LEFT)
botton3.pack(side=LEFT)
botton4.pack(side=BOTTOM)



root.mainloop() # to keep the window in a loop that enables it to show# %%


