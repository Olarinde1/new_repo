import os, datetime, csv
# os.remove('text.txt')
# os.rename('text.txt', 'renamed.txt')
print(os.path.exists('renamed.txt'))
print(os.path.exists('text.txt'))
print(os.path.getsize('renamed.txt'))
print(os.path.getsize('introduction.py'))
print(os.path.getsize('os.py'))
timestamp_1 = os.path.getmtime('renamed.txt')
timestamp_2 = os.path.getmtime('introduction.py')
timestamp_3 = os.path.getmtime('os.py')
real_time_1 = datetime.datetime.fromtimestamp(timestamp_1)
real_time_2 = datetime.datetime.fromtimestamp(timestamp_2)
real_time_3 = datetime.datetime.fromtimestamp(timestamp_3)
print(real_time_1)
print(real_time_2)
print(real_time_3)


file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
    print(os.path.isfile(file))
    print("File not found")
print(os.path.abspath('introduction.py'))
# print(os.getcwd())
# os.mkdir('new_dir')
os.chdir("C:\\Users\\DELL\\Desktop\\Tkinter\\new_repo")
print(os.getcwd())
# os.mkdir('newer_dir')
# os.rmdir('newer_dir')
# print(os.listdir("OS_cousera"))
directory = "OS_cousera" 
for name in os.listdir(directory):
    fullname = os.path.join(directory, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

# os.chdir("..")
# print(os.getcwd())

# import os


# def new_directory(directory, filename):
#   # Before creating a new directory, check to see if it already exists
#   if os.path.isdir(directory) == False:
#     os.mkdir(directory)
    

#   # Create the new file inside of the new directory
#   os.chdir(directory)
#   with open (filename, 'w') as file:
#     file.write("")

#   # Return the list of files in the new directory
#   os.chdir("..")
#   return os.listdir(directory)

# print(new_directory("PythonPrograms", "script.py"))
# import os
# import datetime

# def file_date(filename):
#   # Create the file in the current directory
#   with open(filename, 'w') as file:
#     file.write("")

#   timestamp = os.path.getmtime(filename)
#   # Convert the timestamp into a readable format, then into a string
#   real_time = datetime.datetime.fromtimestamp(timestamp)
#   time = str(real_time)
#   # Return just the date portion 
#   # Hint: how many characters are in “yyyy-mm-dd”? 
#   return ("{}".format(time[0:11]))

# print(file_date("newfile.txt")) 
# # Should be today's date in the format of yyyy-mm-dd
# os.chdir("C:\\Users\\DELL\\Desktop\\Tkinter\\new_repo\\OS_cousera")
print(os.getcwd())
print(os.listdir('OS_cousera'))
os.chdir("OS_cousera\\new_dir")
# with open('csv.txt', 'w') as file:
#     file.write("Alli Olarinde, 0001221120, Developer")

