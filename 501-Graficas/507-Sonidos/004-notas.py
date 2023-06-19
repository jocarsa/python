#pip install playsound
import threading
from playsound import playsound
import os
import time

directorio = 'mp3/'
notas = []
for archivo in os.listdir("mp3"):
    if os.path.isfile(os.path.join(directorio, archivo)):
        notas.append(directorio+archivo)

def alert():
    threading.Thread(target=playsound, args=('mp3/A4.mp3',), daemon=True).start()
    

def bucle():
    alert()
    time.sleep(1)
    bucle()

bucle()


