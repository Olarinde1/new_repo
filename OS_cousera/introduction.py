#!/usr/bin/env python
import requests
import shutil, psutil
import PIL.Image as pi
import arrow
import pandas as pd
response = requests.get("https://www.google.com")
print(response)
if response.status_code == 200:
    print('Ok')
date = arrow.get("2020-11-26", "YYYY-MM-DD")
new_date = date.shift(weeks=+6).format("MMM DD YYYY")
print(new_date)
# image = pi.open('houses.jpg')
# print(image.size)
visitors = [1223, 123, 13342, 33321, 1112]
errors = [23, 45, 33, 11, 98]
df = pd.DataFrame({'visitors': visitors, 'errors':errors}, index=['Mon', 'Tues', 'Wed', 'Thur', 'Fri'])
print(df)
print(df.errors.mean())
disk_usage = shutil.disk_usage('/')
print(disk_usage)
print(disk_usage.free/disk_usage.total * 100)

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage('/') or not check_cpu_usage():
    print('ERROR!!!')
else:
    print("Everything is OK")