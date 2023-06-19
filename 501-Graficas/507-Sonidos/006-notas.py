#pip install playsound==1.2.2
import threading
from playsound import playsound
import os
import time
import random as rand

directorio = 'mp3/'
notas = []
reproducciones = []
for archivo in os.listdir("mp3"):
    if os.path.isfile(os.path.join(directorio, archivo)):
        notas.append(directorio+archivo)

def alert():
    longitud = len(notas)
    aleatorio = rand.randint(0,longitud)
    reproducciones.append(threading.Thread(target=playsound, args=(notas[aleatorio],), daemon=True).start())

def cierra():
    print("voy a cerrar")

def bucle():
    alert()
    time.sleep(1)
    bucle()

bucle()


