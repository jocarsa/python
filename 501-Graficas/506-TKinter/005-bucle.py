import time
import tkinter as tk
import random

def bucle():
    print("hola")
    x = random.randint(0,512)
    y = random.randint(0,512)
    lienzo.create_rectangle(x,y,x+10,y+10,fill="red")
    time.sleep(1)
    bucle()


raiz = tk.Tk()
raiz.geometry("512x512")
lienzo = tk.Canvas()
lienzo.pack()




bucle()
