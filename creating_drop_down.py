from tkinter import *

def doNothing():
    print('created this for testing')
#  Creating a main Menu
root = Tk()
myMenu = Menu(root)
root.config(menu=myMenu)

subMenu = Menu(myMenu)
myMenu.add_cascade(label='File', menu=subMenu)

subMenu.add_command(label='New project..', command=doNothing)
subMenu.add_command(label='New ..', command=doNothing)
subMenu.add_separator()
subMenu.add_command(label='Exit', command=doNothing)

editMenu = Menu(myMenu)
myMenu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='redo...', command=doNothing)

# creating Toolbar

toolbar = Frame(root, bg='blue')
insertButton = Button(toolbar, text="insert something", command=doNothing)
insertButton.pack(side=LEFT, padx=2, pady=2)
printButton = Button(toolbar, text="print something", command=doNothing)
printButton.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

# creating status bar
statusBar = Label(root, text='Preparing to do something',bd=1, relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)

root.mainloop()