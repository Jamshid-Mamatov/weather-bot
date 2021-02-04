import os 
import json
from pprint import pprint
import requests
token=os.environ['token']



def getUpdate_text():
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    r=requests.get(url)
    data=r.json()['result']
    
    text=data[-1]['message']['text']
    if text=='/start':
        text='*shaxaringizni kiriting*'
        sendMsg(text)
    else:
        weather(text)

def getUpdate_id():
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    r=requests.get(url)

    data=r.json()['result']
    chat_id=data['message']['chat']['id']
    return chat_id


def weather(text):
    api_key='f9716fd07196bb4a858f3d8cddfec94d'
    url=f'http://api.openweathermap.org/data/2.5/forecast'
    payload={
        'q':text,
        'appid':api_key
    }
    r=requests.get(url,params=payload)

    data=r.json()
    if r.status_code==200:

        text=text.title()
        inform=data['list'][-1]
        temp=inform['main']['temp']-273.15
        description=inform['weather'][0]['description']
        wind=inform['wind']['speed']
        weather=f"from:*{text}*\nTemp:{temp}\ndescription:{description}\nwind:{wind}m/s"
        sendMsg(weather)
    else:
        weather='city not found'
        sendMsg(weather)


def sendMsg(text):
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    chat_id=getUpdate_id()
    payload={
        'chat_id':chat_id,
        'text':text,
        'parse_mode':'MarkdownV2 '

    }
    r=requests.get(url)


