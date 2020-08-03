from tkinter import *
import sqlite3
import json
from PIL import ImageTk,Image
from tkinter import filedialog
root = Tk()
root.title('Polymath Tech')
root.iconbitmap('C:/Users/DELL/Desktop/Tkinter/new_repo/codemy/umbrella.ico')
root.geometry("400x400")

# creating or connecting to a database

# # creating a table
# cursor.execute("""CREATE TABLE addresses (
#     first_name text,
#     last_name text, 
#     address text, 
#     city text, 
#     state text, 
#     zipcode integer
#     )""")

# # commiting changes


# creating submit boxes
def submit():
    conn = sqlite3.connect('address_book.db')
    # creating cursor
    cursor = conn.cursor()

    # inisering into table
    cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", 
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                "address": address.get(),
                "city": city.get(),
                "state": state.get(),
                'zipcode': zip_code.get()
            }
    )
    conn.commit()
    conn.close()



    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip_code.delete(0, END)
# creating quety function
def query():
    conn = sqlite3.connect('address_book.db')
    # creating cursor
    cursor = conn.cursor()
    # query the database
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()
    # print(records)

    # looping through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)


    conn.commit()
    conn.close()

# create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)


l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)


address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)


zip_code = Entry(root, width=30)
zip_code.grid(row=5, column=1, padx=20)


# creating text box labels

f_name_label = Label(root, text='first Name: ')
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text='last Name: ')
l_name_label.grid(row=1, column=0)

address_label = Label(root, text='Address: ')
address_label.grid(row=2, column=0)

city_label = Label(root, text='City: ')
city_label.grid(row=3, column=0)

state_label = Label(root, text='State: ')
state_label.grid(row=4, column=0)

zip_code_label = Label(root, text='Zipcode: ')
zip_code_label.grid(row=5, column=0)

# creating submit buttons
submit_btn = Button(root, text='Add record to database', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# creating a query button
query_btn = Button(root, text='show record', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=130)



root.mainloop()
