import tkinter as interfaz
from tkinter import ttk
from tkinter.messagebox import showinfo

raiz = interfaz.Tk()
raiz.geometry("300x300")

arbol = ttk.Treeview()
e1 = arbol.insert("", interfaz.END, text="Elemento 1")
e2 = arbol.insert("", interfaz.END, text="Elemento 2")
e3 = arbol.insert("", interfaz.END, text="Elemento 3")
e4 = arbol.insert("", interfaz.END, text="Elemento 4")
arbol.insert(e4, interfaz.END, text="Subelemento 1")
arbol.insert(e4, interfaz.END, text="Subelemento 2")
arbol.insert(e4, interfaz.END, text="Subelemento 3")
arbol.pack()





