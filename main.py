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
    
    return text


def getchat_id():
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    r=requests.get(url)

    data=r.json()['result']
    chat_id=data[-1]['message']['chat']['id']
    return chat_id


def weather():
    api_key='f9716fd07196bb4a858f3d8cddfec94d'
    url=f'http://api.openweathermap.org/data/2.5/forecast'
    text=getUpdate_text()
    payload={
        'q':text,
        'appid':api_key
    }
    r=requests.get(url,params=payload)

    data=r.json()
    if r.status_code==200:

        text=text.title()
        inform=data['list'][-1]
        temp=int(inform['main']['temp']-273.15)
        description=inform['weather'][0]['description']
        wind=inform['wind']['speed']
        weather=f"from:{text}\nTemp:{temp}\ndescription:{description}\nwind:{wind}m/s"   
    else:
        weather='city not found'
    

    return weather


def sendMsg():
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    chat_id=getchat_id()
    text=weather()
    print(text)
    payload={
        'chat_id':chat_id,
        'text':text,
    }
    r=requests.get(url,payload)

def updateId():
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    r=requests.get(url)

    data=r.json()['result']
    update_id=data[-1]['update_id']
    return update_id


last_update_id=None
while True:
    new_update_id=updateId()
    if last_update_id!=new_update_id:
        sendMsg()
        
        last_update_id=new_update_id
        


    
