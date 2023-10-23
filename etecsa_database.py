import requests
import json
import pandas as pd
import telebot
from telebot.types import ReplyKeyboardMarkup
from settings import *

bot = telebot.TeleBot(TELEGRAM_TOKEN)



def numero_telefonico(message):
    msg = bot.send_message(message.chat.id,"Digame cual es el numero")
    return msg
    
    
def registro(message):
    
    nombres = []
    numeros = []
    direcciones = []
    locations = []
    
    number = message.text
    website = f'https://directorioetecsa.com/api/search?q={number}&offset=0&limit=10000'
    result = requests.get(website).text
    lista = json.loads(result)
    # print(lista['data'][0]['name'])
    lista = lista['data']
    print(len(lista))
    if len(lista) > 0:
        for dato in lista:
            nombres.append(dato['name'])
            numeros.append(dato['number'])
            direcciones.append(dato['address'])
            locations.append(dato['location'])
        df = pd.DataFrame({'Nombres':nombres,'Numero':numeros})
        bot.send_message(message.chat.id,f"{df}")
        
        df = pd.DataFrame({'Nombres':nombres,'Numero':numeros,'Direcciones':direcciones,'Ubicacion GPS':locations})
        df.to_csv('informacion.csv')
        document = open('informacion.csv')
        bot.send_document(message.chat.id,document)
        # print(lista)    
    else:
        print(f'No existe ningun {number}')
        bot.send_message(message.chat.id,f'No se ha encontrado ningun <b>{number}</b>',parse_mode='html')
        
    
    # df = pd.DataFrame({'Nombres':nombres,'Numero':numeros})
    # bot.send_message(message.chat.id,f"{df}")
    
    # df = pd.DataFrame({'Nombres':nombres,'Numero':numeros,'Direcciones':direcciones,'Ubicacion GPS':locations})
    # df.to_csv('informacion.csv')
    # document = open('informacion.csv')
    # bot.send_document(message.chat.id,document)
    # print(df)

# dh = pd.DataFrame([nombres,numeros,direcciones,locations])
# dh.to_excel('tabla.xlsx')