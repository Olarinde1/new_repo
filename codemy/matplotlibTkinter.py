from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Polymath Tech')
root.iconbitmap('C:/Users/DELL/Desktop/Tkinter/new_repo/codemy/umbrella.ico')
root.geometry("400x400")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.polar(house_prices)
    plt.show()

btn = Button(root, text='show plot', command=graph)
btn.pack()

root.mainloop()