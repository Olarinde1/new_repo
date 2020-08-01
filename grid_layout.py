from tkinter import *
root = Tk()

name = Label(root, text='Name: ')
password = Label(root, text='Password: ')
name_entry = Entry(root)
pass_entry = Entry(root)

name.grid(row=0, sticky=E)
password.grid(row=1, sticky=E)

name_entry.grid(row=0, column=1)
pass_entry.grid(row=1, column=1)

check = Checkbutton(root, text='keep me logged in')
check.grid(columnspan=2)
root.mainloop()