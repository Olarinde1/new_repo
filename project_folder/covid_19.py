import requests as rq
from win10toast import ToastNotifier
import json
import time

def update():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    text = f'confimed cases: {data["cases"]} \nDeaths'