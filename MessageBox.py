from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Polymath Window", 'testing messagebox.')

answer = tkinter.messagebox.askquestion('Question 1', 'are you okay?..')
if answer == 'yes':
    print("that's good!")
else:
    print('please take care of yourself')

root.mainloop()