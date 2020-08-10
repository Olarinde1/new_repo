from tkinter import *
import sqlite3
import json
from PIL import ImageTk,Image
from tkinter import filedialog
root = Tk()
root.title('Polymath Tech')
root.iconbitmap('C:/Users/DELL/Desktop/Tkinter/new_repo/codemy/umbrella.ico')
root.geometry("400x600")

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

# creating a function to delete record

def delete():
    conn = sqlite3.connect('address_book.db')
    # creating cursor
    cursor = conn.cursor()

    cursor.execute("DELETE from addresses WHERE oid= " + delete_box.get())
    conn.commit()
    conn.close()
    delete_box.delete(0, END)

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
    conn.closeditor


    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip_code.delete(0, END)

# creating the update function
def update():
    conn = sqlite3.connect('address_book.db')
    # creating cursor
    cursor = conn.cursor()
    # record_id = delete_box.get()
    cursor.execute("""UPDATE addresses SET
            first_name = :first, 
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode
            
            WHERE oid = :oid""",
            {
                'first': f_name_editor.get(),
                'last': l_name_editor.get(),
                'address': address_editor.get(),
                'city': city_editor.get(),
                'state': state_editor.get(),
                'zipcode': zip_code_editor.get(),
                'oid': record_id
            }
    
        )
    
    conn.commit()
    conn.close()    
    editor.destroy()

# creating edit function
def edit():
    global editor
    editor = Tk()
    editor.title('Polymath Tech')
    editor.iconbitmap('C:/Users/DELL/Desktop/Tkinter/new_repo/codemy/umbrella.ico')
    editor.geometry("400x200")

    conn = sqlite3.connect('address_book.db')
    # creating cursor
    global record_id
    cursor = conn.cursor()
    record_id = delete_box.get()
    # query the database
    cursor.execute("SELECT * FROM addresses WHERE OID = " + record_id)
    records = cursor.fetchall()
    # looping through results
    # print(records)
    # creating global variables for text boxes names

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zip_code_editor
    
    # create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))


    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)


    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)


    zip_code_editor = Entry(editor, width=30)
    zip_code_editor.grid(row=5, column=1, padx=20)

    # creating text box labels

    f_name_label = Label(editor, text='first Name:')
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    l_name_label = Label(editor, text='last Name:')
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text='Address:')
    address_label.grid(row=2, column=0)

    city_label = Label(editor, text='City:')
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text='State:')
    state_label.grid(row=4, column=0)

    zip_code_label = Label(editor, text='Zipcode:')
    zip_code_label.grid(row=5, column=0)
    # creating a save button to save edited records
    
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zip_code_editor.insert(0, record[5])

    save_btn = Button(editor, text='Save record', command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=134)

   

# creating query function
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
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)


    conn.commit()
    conn.close()

# create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))


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

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# creating text box labels

f_name_label = Label(root, text='first Name:')
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text='last Name:')
l_name_label.grid(row=1, column=0)

address_label = Label(root, text='Address:')
address_label.grid(row=2, column=0)

city_label = Label(root, text='City:')
city_label.grid(row=3, column=0)

state_label = Label(root, text='State:')
state_label.grid(row=4, column=0)

zip_code_label = Label(root, text='Zipcode:')
zip_code_label.grid(row=5, column=0)

delete_box_label = Label(root, text='Select ID')
delete_box_label.grid(row=9, column=0, pady=5)
# creating submit buttons
submit_btn = Button(root, text='Add record to database', command=submit)

submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# creating a query button
query_btn = Button(root, text='show record', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=130)

# creating a delete butoon

delete_btn = Button(root, text='Delete record', command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=128)

# creating an update button
edit_btn = Button(root, text='Edit record', command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=134)



root.mainloop()
