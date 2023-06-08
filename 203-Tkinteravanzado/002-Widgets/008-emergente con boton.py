import tkinter as interfaz
from tkinter import ttk
from tkinter.messagebox import showinfo

raiz = interfaz.Tk()
raiz.geometry("300x300")

def problemas():
    interfaz.messagebox.showinfo(
        title="Problema",
        message="Ha ocurrido algún tipo de problema"
    )

boton = interfaz.Button(text="Pulsame",command=problemas).pack()





