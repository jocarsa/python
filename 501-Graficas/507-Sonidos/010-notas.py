import tkinter as tk
import random as rand
import math
import threading
from playsound import playsound
import os
import time

anchura = 300


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
        self.x = anchura/2
        self.y = anchura/2
        rojo = rand.randint(0, 255)
        verde = rand.randint(0, 255)
        azul = rand.randint(0, 255)
        self.color = rgb_to_hex(rojo, verde, azul)
        self.direccion = rand.randint(0, 365)
    def mueve(self):
        self.x += math.cos(self.direccion)*5
        self.y+=math.sin(self.direccion)*5
        if self.x < 0 or self.y < 0 or self.x > anchura or self.y > anchura:
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
            if personas[i].x < 0 or personas[i].y < 0 or personas[i].x > anchura or personas[i].y > anchura:
                tocaNota(i)
        self.master.after(10,self.bucle)
raiz = tk.Tk()
raiz.geometry(str(anchura)+"x"+str(anchura))
raiz.configure(bg='black')
lienzo = tk.Canvas(width=anchura, height=anchura)
lienzo.configure(bg='black')
lienzo.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

aplicacion = Aplicacion(raiz)


