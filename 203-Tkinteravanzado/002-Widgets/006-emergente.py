import tkinter as interfaz
from tkinter import ttk

raiz = interfaz.Tk()
raiz.geometry("300x300")

opcion = interfaz.IntVar()

ttk.Radiobutton(text="opción 1",variable=opcion,value=1).pack()
ttk.Radiobutton(text="opción 2",variable=opcion,value=2).pack()
ttk.Radiobutton(text="opción 3",variable=opcion,value=3).pack()
ttk.Radiobutton(text="opción 4",variable=opcion,value=4).pack()

opcion2 = interfaz.IntVar()

ttk.Radiobutton(text="opción a",variable=opcion2,value=1).pack()
ttk.Radiobutton(text="opción b",variable=opcion2,value=2).pack()
ttk.Radiobutton(text="opción c",variable=opcion2,value=3).pack()
ttk.Radiobutton(text="opción d",variable=opcion2,value=4).pack()




