from tkinter import *

root = Tk()
root.title("Simple calculator")
entry = Entry(root, width=50,bg='white', borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
def buttonClick(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def buttonClear():
    entry.delete(0, END)

def buttonAdd():
    global first_number
    first_number = entry.get()
    global f_num
    global math
    math = 'addition'
    f_num = eval(first_number)
    entry.delete(0, END)
    
def buttonEqual():
    second_number = entry.get()
    entry.delete(0, END)
    if math == 'addition':
        entry.insert(0, f_num + eval(second_number))
    if math == 'subtraction':
        entry.insert(0, f_num - eval(second_number))
    if math == 'multiplication':
        entry.insert(0, f_num * eval(second_number))
    if math == 'division':
        entry.insert(0, f_num / eval(second_number))

def buttonSubtract():
    first_number = entry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = eval(first_number)
    entry.delete(0, END)

def buttonMultiply():
    first_number = entry.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = eval(first_number)
    entry.delete(0, END)

def buttonDivide():
    first_number = entry.get()
    global f_num
    global math
    math = 'division'
    f_num = eval(first_number)
    entry.delete(0, END)

# <--------creating/defining buttons------------>

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1), bg='white')
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2), bg='white')
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3), bg='white')
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4), bg='white')
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5), bg='white')
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6), bg='white')
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7), bg ='white')
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8), bg ='white')
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9), bg ='white')
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0), bg ='white')
button_add = Button(root, text="+", padx=39, pady=20, command=buttonAdd, bg='white')
button_equal = Button(root, text="=", padx=95, pady=20, command=buttonEqual, bg= 'white')
button_clear = Button(root, text="Clear", padx=85, pady=20, command=buttonClear, bg='white')
button_subtract = Button(root, text="-", padx=40, pady=20, command=buttonSubtract, bg='white')
button_multiply = Button(root, text="x", padx=40, pady=20, command=buttonMultiply, bg='white')
button_divide = Button(root, text="/", padx=40, pady=20, command=buttonDivide, bg='white')

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
