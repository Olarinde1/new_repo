from tkinter import *
import sqlite3
import json
from PIL import ImageTk,Image
from tkinter import filedialog
root = Tk()
root.title('Polymath Tech')
root.iconbitmap('C:/Users/23480/Desktop/Datascience/Tkinter/codemy/umbrella.ico')
root.geometry("400x400")

# creating or connecting to a database
conn = sqlite3.connect('address_book.db')
# creating cursor
cursor = conn.cursor()
# creating a table
cursor.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text, 
    address text, 
    city text, 
    state text, 
    zipcode integer
    )""")

# commiting changes
conn.commit()

# closing connectinon

conn.close()



root.mainloop()