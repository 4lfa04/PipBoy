import telebot
import time
import datetime
from settings import *
import threading
from telebot.types import ReplyKeyboardMarkup # Es la libreria para crear botones
from telebot.types import ForceReply # Es la libreria citar mensajes
from telebot.types import ReplyKeyboardRemove

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def ayuda_mensaje(message):

    test = ReplyKeyboardRemove()
    
    print(message.text)
    bot.send_chat_action(message.chat.id, "typing")
    if message.text == "✉️ Iniciar Sesion":
        print("Ayuda sobre iniciar sesion")
        bot.send_message(message.chat.id, "Tranquilo, esta funcion aun está en desarrollo, vuelve dentro de unos dias", reply_markup=test)
    if message.text == "🤖 Chat GPT":
        bot.send_message(message.chat.id,'<a href="https://t.me/gpt3_unlim_chatbot">Chat GPT</a>', parse_mode='html', reply_markup=test)
    if message.text == "🌐 Pagina Web":
        pass
    
    