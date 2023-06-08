import tkinter as interfaz
from tkinter import ttk

raiz = interfaz.Tk()
raiz.geometry("300x300")

def comprueba():
    print("Vamos a comprobar")

ttk.Checkbutton(text="Acepto",command=comprueba).pack()




