import tkinter as tk
import random as rand
import math

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
        
persona1 = Persona()
print(persona1)
class Aplicacion(object):
    def __init__(self,master):
        self.master = master
        self.master.after(1000,self.bucle)
    def bucle(self):
        persona1.mueve()
        persona1.dibuja()
        self.master.after(100,self.bucle)
raiz = tk.Tk()
raiz.geometry("512x512")
lienzo = tk.Canvas(width=512, height=512)
lienzo.pack()

aplicacion = Aplicacion(raiz)


