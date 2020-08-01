from tkinter import *

root = Tk()
root.title('Frames')
root.iconbitmap('C:/Users/23480/Desktop/Datascience/Tkinter/codemy/umbrella.ico')

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

button = Button(frame, text='Dont click here')
button2 = Button(frame, text='..... or here')
button.grid(row=0, column=0)
button2.grid(row=1, column=0)


root.mainloop()