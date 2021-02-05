import requests
import json
import tkinter as tk


resp = requests.get('https://www.balldontlie.io/api/v1/players')

#Converts response to JSON
data = resp.json()

print(data)

resp = requests.get('https://www.balldontlie.io/api/v1/players/<237>')


lebronjames = resp.json()

print(lebronjames)
