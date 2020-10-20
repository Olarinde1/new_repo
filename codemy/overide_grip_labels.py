from tkinter import *

root = Tk()

root.title("Polymath Tech")
root.iconbitmap('C:/Users/DELL/Desktop/Tkinter/new_repo/codemy/umbrella.ico')
root.geometry("400x400")
myLabel = Label(root)

def myDelete():
    # if myLabel.winfo_exists() == 1:
    #     myLabel.destroy()
    # else:
    #     pass

    myLabel.grid_forget()
    # myLabel.destroy()
    myButton['state'] = NORMAL
    # print(myButton.winfo_exists())

def myClick():
    global myLabel
    myLabel.destroy()
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.grid(row=3, column=0, pady=10)
    # myButton['state']= DISABLED

e = Entry(root, width=17, font=('helveitca', 30))
e.grid(row=0, column=0, pady=10, padx=10)

myButton = Button(root, text='Enter your name', command=myClick)
myButton.grid(row=1, column=0, pady=10)

deleteButton = Button(root, text='Delete Text', command=myDelete)
deleteButton.grid(row=2, column=0, pady=10)
root.mainloop()