from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector

root = Tk()
root.title('Polymath Tech')
root.iconbitmap('C:/Users/DELL/Desktop/Tkinter/new_repo/codemy/umbrella.ico')
root.geometry("400x600")
# connecting to MySQL  
myDb = mysql.connector.connect(
   host = "localhost",
   user = "root",
   passwd = "Alli@12345",
   database = "Polymath",
)

# print(myDb)
# creating a cursor and initializing it
my_cursor = myDb.cursor()

# creating a database
# my_cursor.execute("CREATE DATABASE Polymath")
# Testing to see if the database was successfully created

# for db in my_cursor:
#    print(db)

# drop table
# my_cursor.execute("DROP TABLE customers")
# creating a table

# my_cursor.execute("CREATE TABLE IF NOT EXIsTS customers (first_name VARCHAR(255),\
#    last_name VARCHAR(255),\
#    zipcode INT(10),\
#    price_paid DECIMAL(10, 2),\
#    user_id INT AUTO_INCREMENT PRIMARY KEY)")

# # altering table
# my_cursor.execute("ALTER TABLE customers ADD (\
# email VARCHAR(255),\
# address_1 VARCHAR(255),\
# address_2 VARCHAR(255),\
# city VARCHAR(50),\
# state VARCHAR(50),\
# country VARCHAR(255),\
# phone VARCHAR(255),\
# username VARCHAR(255),\
# payment_method VARCHAR(50),\
# discount_code VARCHAR(255))")
# # show table
# my_cursor.execute('SELECT * FROM customers')

# print(my_cursor.description)
# for x in my_cursor.description:

def clear_fields():
   first_name_box.delete(0, END)
   last_name_box.delete(0, END)
   address1_box.delete(0, END)
   address2_box.delete(0, END)
   city_box.delete(0, END)
   state_box.delete(0, END)
   zipcode_box.delete(0, END)
   country_box.delete(0, END)
   phone_box.delete(0, END)
   email_box.delete(0, END)
   username_box.delete(0, END)
   payment_method_box.delete(0, END)
   discount_code_box.delete(0, END)
   price_paid_box.delete(0, END)

# submitting customer to database
def add_customer():
   sql_command = "INSERT INTO customers (first_name, last_name, address_1, address_2, city, state, zipcode, country, phone, email, username, payment_method, discount_code, price_paid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
   values = (first_name_box.get(), last_name_box.get(), address1_box.get(), address2_box.get(), city_box.get(), state_box.get(), zipcode_box.get(), country_box.get(), phone_box.get(), email_box.get(), username_box.get(), payment_method_box.get(), discount_code_box.get(), price_paid_box.get())
   my_cursor.execute(sql_command, values)
   myDb.commit()
   clear_fields()
#    print(x)
# creating a label
title_label = Label(root, text='Polymath Customer Database', font=('Helvetica', 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)
# create main form to enter customer data
first_name_label = Label(root, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
last_name_label = Label(root, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
address1_label = Label(root, text="Address 1").grid(row=3, column=0, sticky=W, padx=10)
address2_label = Label(root, text="Address 2").grid(row=4, column=0, sticky=W, padx=10)
city_label = Label(root, text="City").grid(row=5, column=0, sticky=W, padx=10)
state_label = Label(root, text="State").grid(row=6, column=0, sticky=W, padx=10)
zipcode_label = Label(root, text="Zipcode").grid(row=7, column=0, sticky=W, padx=10)
country_label = Label(root, text="Country").grid(row=8, column=0, sticky=W, padx=10)
phone_label = Label(root, text="Phone Number").grid(row=9, column=0, sticky=W, padx=10)
email_label = Label(root, text="Email Address").grid(row=10, column=0, sticky=W, padx=10)
username_label = Label(root, text="Username").grid(row=11, column=0, sticky=W, padx=10)
payment_method_label = Label(root, text="Payment Method").grid(row=12, column=0, sticky=W, padx=10)
discount_code_label = Label(root, text="Discount Code").grid(row=13, column=0, sticky=W, padx=10)
price_paid_label = Label(root, text="Price Paid").grid(row=14, column=0, sticky=W, padx=10)

# entry boxes
first_name_box = Entry(root)
first_name_box.grid(row=1, column=1)

last_name_box = Entry(root)
last_name_box.grid(row=2, column=1, pady=5)

address1_box = Entry(root)
address1_box.grid(row=3, column=1, pady=5)

address2_box = Entry(root)
address2_box.grid(row=4, column=1, pady=5)

city_box = Entry(root)
city_box.grid(row=5, column=1, pady=5)

state_box = Entry(root)
state_box.grid(row=6, column=1, pady=5)

zipcode_box = Entry(root)
zipcode_box.grid(row=7, column=1, pady=5)

country_box = Entry(root)
country_box.grid(row=8, column=1, pady=5)

phone_box = Entry(root)
phone_box.grid(row=9, column=1, pady=5)

email_box = Entry(root)
email_box.grid(row=10, column=1, pady=5)

username_box = Entry(root)
username_box.grid(row=11, column=1, pady=5)

payment_method_box = Entry(root)
payment_method_box.grid(row=12, column=1, pady=5)

discount_code_box = Entry(root)
discount_code_box.grid(row=13, column=1, pady=5)

price_paid_box = Entry(root)
price_paid_box.grid(row=14, column=1, pady=5)

# creating buttons
add_customer_btn = Button(root, text="Add Customer To Database", command=add_customer)
add_customer_btn.grid(row=15, column=0, padx=10, pady=10)
clear_fields_button = Button(root, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=15, column=1)

my_cursor.execute("SELECT * FROM customers")
result = my_cursor.fetchall()
for x in result:
   print(x)
root.mainloop() 
