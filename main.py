import os 
import json
from pprint import pprint
import requests
token=os.environ['token']

api_key=
url=f"http://api.openweathermap.org/data/2.5/forecast"
#http://api.openweathermap.org/data/2.5/forecast?q=jizzax&appid=f9716fd07196bb4a858f3d8cddfec94d
def getUpdate():
    url=f'https://api.telegram.org/bot{token}/getUpdate'
    r=requests.get(url)
    data=r.json()['result']
    text=data[-1]['message']['text']
    weather(text)

def weather(text):
    api_key='f9716fd07196bb4a858f3d8cddfec94d'
    url=f'http://api.openweathermap.org/data/2.5/forecast'
    payload={
        'q':text,
        'appid':api_key
    }
    r=requests.get(url,params=payload)



print(requests.get(url))

