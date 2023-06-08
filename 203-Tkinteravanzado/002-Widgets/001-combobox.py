import tkinter as interfaz
from tkinter import ttk

raiz = interfaz.Tk()
raiz.geometry("300x300")

marco = interfaz.Frame(raiz)
marco.pack()

desplegable = ttk.Combobox(marco)
desplegable['values']= ['uno','dos','tres','cuatro','cinco','seis','siete']
desplegable.pack()




