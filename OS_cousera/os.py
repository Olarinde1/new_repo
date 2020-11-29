import os, datetime
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
os.chdir('new_dir')
print(os.getcwd())