import telebot
import time
# import datetime
from settings import *

from datetime import datetime, timedelta
from threading import Thread
from time import sleep

bot = telebot.TeleBot(TELEGRAM_TOKEN)

class Temporizador(Thread):
    def __init__(self, hora, delay, message, texto):
        super(Temporizador, self).__init__()
        self._estado = True
        self.hora = hora
        self.delay = delay
        self.message = message
        self.texto = texto

    def stop(self):
        self._estado = False

    def run(self):
        aux = datetime.strptime(self.hora, '%H:%M:%S')
        hora = datetime.now()
        hora = hora.replace(hour = aux.hour, minute=aux.minute, second=aux.second, microsecond = 0)
        if hora <= datetime.now():
            hora += timedelta(days=1)

        while self._estado:
            if hora <= datetime.now():
                # self.funcion()
                print('Función ejecutada desde hilo')
                bot.send_message(self.message, self.texto)
                hora += timedelta(days=1)
            sleep(self.delay)



#=========================================================================================
#Ejemplo de uso:

def ejecutar(message):
    print('Función ejecutada desde hilo')
    bot.send_message(841744845,"Buenas Noches")
def start_temporizador(message):
    t = Temporizador('15:00:30',1,message.chat.id,"Buenas Noches🌙\nCreo que es hora de que tengamos una pequeña charla")# Instanciamos nuestra clase Temporizador
    t.start() #Iniciamos el hilo

    #Mientras el programa principal puede seguir funcinando:
    # sleep(2)
    # for _ in range(10):
    #     print('Imprimiendo desde hilo principal')
    #     sleep(2)

    # # Si en cualquier momento queremos detener el hilo desde la aplicacion simplemete usamos el método stop()
    # sleep(120) # Simulamos un tiempo de espera durante el cual el programa principal puede seguir funcionando. 
    # t.stop()   # Detenemos el hilo.