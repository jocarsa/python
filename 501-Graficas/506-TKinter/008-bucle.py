import tkinter as tk
import random

class Aplicacion(object):
    def __init__(self,master):
        self.master = master
        self.master.after(1000,self.bucle)
    def bucle(self):
        x = random.randint(0,512)
        y = random.randint(0,512)
        lienzo.create_rectangle(x,y,x+10,y+10,fill="red")
        #print("el programa ha arrancando y empezará a dar vueltas")
        lienzo.create_rectangle(10,10,20,20,fill="red")
        self.master.after(100,self.bucle)
raiz = tk.Tk()
raiz.geometry("512x512")
lienzo = tk.Canvas(width=512, height=512)
lienzo.pack()

aplicacion = Aplicacion(raiz)


