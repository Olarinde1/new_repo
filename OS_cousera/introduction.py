#!/usr/bin/env python
import requests
import shutil
import PIL.Image as pi
import arrow
import pandas as pd
response = requests.get("https://www.google.com")
print(len(response.text))
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