import requests
import json
import tkinter as tk


resp = requests.get('https://www.balldontlie.io/api/v1/players')

#Converts response to JSON
data = resp.json()

print(data)
