import tkinter as tk
import random as rand

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

class Aplicacion(object):
    def __init__(self,master):
        self.master = master
        self.master.after(1000,self.bucle)
    def bucle(self):
        x = rand.randint(0,512)
        y = rand.randint(0,512)
        rojo = rand.randint(0, 255)
        verde = rand.randint(0, 255)
        azul = rand.randint(0, 255)
        micolor = rgb_to_hex(rojo, verde, azul)
        lienzo.create_rectangle(x,y,x+10,y+10,fill=micolor)
        #print("el programa ha arrancando y empezará a dar vueltas")
        lienzo.create_rectangle(10,10,20,20,fill="red")
        self.master.after(100,self.bucle)
raiz = tk.Tk()
raiz.geometry("512x512")
lienzo = tk.Canvas(width=512, height=512)
lienzo.pack()

aplicacion = Aplicacion(raiz)


