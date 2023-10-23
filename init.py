import telebot
import time
import datetime
from settings import *
import threading
import funciones
import etecsa_database
import json

# Funciones Especificas
import help_responses

from telebot.types import ReplyKeyboardMarkup # Es la libreria para crear botones
from telebot.types import ForceReply # Es la libreria citar mensajes

import horarias

def programa():
    bot = telebot.TeleBot(TELEGRAM_TOKEN)

    @bot.message_handler(commands=["start"])
    def start_command(message):
        bot.send_chat_action(message.chat.id,'typing')
        funciones.start(message)
        
    @bot.message_handler(commands=["help"])
    def help_command(message):
        bot.send_chat_action(message.chat.id,'upload_photo')
        msg = funciones.help(message)
        bot.register_next_step_handler(msg,help_responses.ayuda_mensaje)
        
    @bot.message_handler(commands=["phone"])
    def phone_command(message):
        bot.send_chat_action(message.chat.id,'typing')
        msg = etecsa_database.numero_telefonico(message)
        bot.register_next_step_handler(msg,etecsa_database.registro)
        
    @bot.message_handler(commands=["signup"])
    def start_command(message):
        bot.send_chat_action(message.chat.id,'typing')
        funciones.signup(message)
        
    @bot.message_handler(commands=['restrat'])
    def restart(message):
        programa()

    @bot.message_handler(commands=['test'])
    def test_message(message):
        funciones.test_message(message)
        
    
    @bot.callback_query_handler(func=lambda x: True)
    def asd(call):
        print(call)
        

    if __name__ == "__main__":
        mensaje = bot.send_message(841744845,"🚀")
        time.sleep(3)
        mensaje = bot.edit_message_text("🚀 Cargando Todas mis Funciones",841744845, mensaje.id)
        bot.set_my_commands([
            telebot.types.BotCommand("/start","Inicia El Bot"),
            telebot.types.BotCommand("/help","Mensaje de Ayuda"),
            telebot.types.BotCommand("/phone","Envia la lista de telefonos resultante"),
            telebot.types.BotCommand("/restart","Reinicia El Bot")
        ])
        
        with open('./assets/db/users.json') as data:
            informacion = json.load(data)
        print(informacion['users'])
        bot.edit_message_text("🚀 Ya estoy cargado, mi amigo", 841744845, mensaje.id)
        print("Todos los sistemas operativos")
        
        bot.infinity_polling()
    
programa()