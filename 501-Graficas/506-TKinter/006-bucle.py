import tkinter as tk

class Aplicacion(object):
    def __init__(self,master):
        self.master = master
        self.master.after(1000,self.bucle)
    def bucle(self):
        print("el programa ha arrancando y empezará a dar vueltas")
        lienzo.create_rectangle(10,10,20,20,fill="red")
        self.master.after(1000,self.bucle)
raiz = tk.Tk()
raiz.geometry("512x512")
lienzo = tk.Canvas()
lienzo.pack()

aplicacion = Aplicacion(raiz)


