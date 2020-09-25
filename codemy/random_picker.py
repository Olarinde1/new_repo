from tkinter import *
from random import randint
root = Tk()

root.title('Polymath Tech')
root.iconbitmap('C:/Users/DELL/Desktop/Tkinter/new_repo/codemy/umbrella.ico')
root.geometry("400x400")
def pick():
    # 6 enteries
    enteries = ['john smith','Alli Olarinde', 'Tom Cruise', 'Alli Olarinde', 'Umar Olarinde', 'Uthman Olarinde', 'Abubakri Olarinde']
    
    # convert to a set
    enteries_set = set(enteries)

    # convert back to a list
    unique_enteries = list(enteries_set)
    # create a random numbe between 0 and 5
    # create a list zize
    our_number = len(unique_enteries) - 1
    rando = randint(0, our_number)

    winnerLabel = Label(root, text=unique_enteries[rando], font=('Helvetica', 18))
    winnerLabel.pack(pady=50)
topLabel = Label(root, text='Winner! ', font=("Helvetica", 24))
topLabel.pack(pady=20)

winButton = Button(root, text= "PICK A WINNER!!!", font=('Helvetica', 24), command= pick)
winButton.pack(pady=20)
root.mainloop()