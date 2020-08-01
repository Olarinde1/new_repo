from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Frames')
root.iconbitmap('C:/Users/23480/Desktop/Datascience/Tkinter/codemy/umbrella.ico')

def popup():
    response = messagebox.showerror("This is my Popup", "Hello world")
    Label(root, text=response).pack()
    # if response == 'yes':
    #     Label(root, text="you clicked Yes!").pack()
    # else:
    #     Label(root, text="you clicked No!").pack()

# showinfo, showwarning,showerror, askquestion, askokcancel, askyesno,askretrycancel, askyesnocancel

Button(root, text="Popup", command=popup).pack()


root.mainloop()