import tkinter as tk
import random as rand
import math
import threading
from playsound import playsound
import os
import time

directorio = 'mp3/'
notas = []
reproducciones = []
for archivo in os.listdir("mp3"):
    if os.path.isfile(os.path.join(directorio, archivo)):
        notas.append(directorio+archivo)

def tocaNota(indice):
    reproducciones.append(threading.Thread(target=playsound, args=(notas[indice],), daemon=True).start())

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

class Persona():
    def __init__(self):
        self.x = 256
        self.y = 256
        rojo = rand.randint(0, 255)
        verde = rand.randint(0, 255)
        azul = rand.randint(0, 255)
        self.color = rgb_to_hex(rojo, verde, azul)
        self.direccion = rand.randint(0, 365)
    def mueve(self):
        self.x += math.cos(self.direccion)*5
        self.y+=math.sin(self.direccion)*5
        if self.x < 0 or self.y < 0 or self.x > 511 or self.y > 511:
            self.direccion += 180
            
    def dibuja(self):
        lienzo.create_oval(
            self.x,
            self.y,
            self.x+10,
            self.y+10,
            fill=self.color
            )
        
personas = []
for i in range(0,int(len(notas)/10)):
    personas.append(Persona())
    

class Aplicacion(object):
    def __init__(self,master):
        self.master = master
        self.master.after(1000,self.bucle)
    def bucle(self):
        lienzo.delete('all')
        for i in range(0,len(personas)):
            personas[i].mueve()
            personas[i].dibuja()
            if personas[i].x < 0 or personas[i].y < 0 or personas[i].x > 511 or personas[i].y > 511:
                tocaNota(i)
        self.master.after(10,self.bucle)
raiz = tk.Tk()
raiz.geometry("512x512")
lienzo = tk.Canvas(width=512, height=512)
lienzo.pack()

aplicacion = Aplicacion(raiz)


