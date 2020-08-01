from tkinter import *
import os
from PIL import ImageTk, Image
root = Tk()
root.title("icons images Exit buttons")
# bitmap = 'umbrella.ico'
# root.iconbitmap(bitmap)
# imgicon = PhotoImage(file=os.path.join("C:/Users/23480/Desktop/Datascience/Tkinter/codemy/",'umbrella.png'))
# root.tk.call('wm', 'iconphoto', root._w, imgicon)
root.iconbitmap('C:/Users/23480/Desktop/Datascience/Tkinter/codemy/umbrella.ico')
img1 = ImageTk.PhotoImage(Image.open("C:/Users/23480/Desktop/Datascience/Tkinter/codemy/umbrella.png"))
img2 = ImageTk.PhotoImage(Image.open("C:/Users/23480/Desktop/Datascience/Tkinter/codemy/Images/git_tutorial1.jpg"))
img3 = ImageTk.PhotoImage(Image.open("C:/Users/23480/Desktop/Datascience/Tkinter/codemy/Images/quadratic.jpg"))
img4 = ImageTk.PhotoImage(Image.open("C:/Users/23480/Desktop/Datascience/Tkinter/codemy/Images/quadratic_2.jpg"))
img5 = ImageTk.PhotoImage(Image.open("C:/Users/23480/Desktop/Datascience/Tkinter/codemy/Images/quadratic_3.jpg"))

image_list = [img1, img2, img3, img4, img5]
status = Label(root, text='Image 1 of '+ str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)

label = Label(image=img1)
label.grid(row=0, column=0, columnspan=3)

def forward(image_num):
    global label
    global button_next
    global button_back

    label.grid_forget()
    label = Label(image=image_list[image_num - 1])
    button_next = Button(root, text=">>", command=lambda: forward(image_num + 1))
    button_back = Button(root, text="<<", command=lambda: backward(image_num - 1))
    if image_num == 5:
        button_next = Button(root, text=">>", state=DISABLED)
    # elif image_num == 1:
    #     button_back = Button(root, text="<<", state=DISABLED)
    #     # label = Label(root, text='you have reach the last image')
        # label.grid(row=2, column=0)

    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)

    # updating status bar
    status = Label(root, text="Image "+str(image_num) +" of "+ str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def backward(image_num):
    global label
    global button_next
    global button_back
    label.grid_forget()
    label = Label(image=image_list[image_num - 1])
    button_next = Button(root, text=">>", command=lambda: forward(image_num + 1))
    button_back = Button(root, text="<<", command=lambda:  backward(image_num - 1))

    if image_num == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    # updating status bar
    status = Label(root, text="Image "+str(image_num) +" of "+ str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<<", command= backward, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_next = Button(root, text=">>", command=lambda : forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_next.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)



root.mainloop()
# Tkinter/__pycache__/codemy/umbrella.ico
# C:/Users/23480/Desktop/Datascience/Tkinter/__pycache__/codemy/umbrella.ico