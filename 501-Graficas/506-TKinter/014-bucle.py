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
        
persona1 = Persona()
print(persona1)
class Aplicacion(object):
    def __init__(self,master):
        self.master = master
        self.master.after(1000,self.bucle)
    def bucle(self):
        persona1.x += math.cos(persona1.direccion)*5
        persona1.y+=math.sin(persona1.direccion)*5
        if persona1.x < 0 or persona1.y < 0 or persona1.x > 511 or persona1.y > 511:
            persona1.direccion += 180
        lienzo.create_oval(
            persona1.x,
            persona1.y,
            persona1.x+10,
            persona1.y+10,
            fill=persona1.color
            )

        lienzo.create_rectangle(10,10,20,20,fill="red")
        self.master.after(100,self.bucle)
raiz = tk.Tk()
raiz.geometry("512x512")
lienzo = tk.Canvas(width=512, height=512)
lienzo.pack()

aplicacion = Aplicacion(raiz)


