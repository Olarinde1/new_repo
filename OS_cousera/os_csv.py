import csv
f = open("C:\\Users\\DELL\\Desktop\\Tkinter\\new_repo\\OS_cousera\\new_dir\\csv.txt")
csv_file = csv.reader(f)
for row in csv_file:
    names, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(names, phone, role))

f.close()
hosts = [['workstation.local',"192.168.24.55"], ['webserver.cloud', "10.2.3.4"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
with open("software.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print("{} has {} users".format(row['name'], row['users']))

users = [{ 'name': "Sol Mansi", "username": "Solm", "department": "IT infrastructure"},
{'name': "Lio Nelson", "username": "lion", 'department': "user Experience Research"},
{'name': "Charlie Grey", "username": 'greyc', 'department': "Development"}]
keys = ["name", 'username', 'department']
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    reader = csv.DictReader(file)
    # Read the rows of the file into a dictionary
    
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))