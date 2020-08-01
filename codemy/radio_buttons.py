from tkinter import *

root = Tk()
root.title('Frames')
root.iconbitmap('C:/Users/23480/Desktop/Datascience/Tkinter/codemy/umbrella.ico')

#r = IntVar()
TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ('Onion', "Onion")
]

pizza = StringVar()
pizza.set('Pepperoni')

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()





# Radiobutton(root, text="option 1", variable=r, value=1,command=lambda : clicked(r.get())).pack()
# Radiobutton(root, text="option 2", variable=r, value=2, command=lambda : clicked(r.get())).pack()

# myLabel = Label(root, text=pizza.get())
# myLabel.pack()
myButton = Button(root, text='click me', command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()