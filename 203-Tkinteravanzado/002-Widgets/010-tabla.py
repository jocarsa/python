import tkinter as interfaz
from tkinter import ttk
from tkinter.messagebox import showinfo

raiz = interfaz.Tk()
raiz.geometry("300x300")

arbol = ttk.Treeview(raiz, column=("Nombre", "Telefono", "Email"), show='headings', height=5)
arbol.column("# 1", anchor=interfaz.CENTER)
arbol.heading("# 1", text="Nombre")
arbol.column("# 2", anchor=interfaz.CENTER)
arbol.heading("# 2", text="Telefono")
arbol.column("# 3", anchor=interfaz.CENTER)
arbol.heading("# 3", text="Email")

# Insert the data in Treeview widget
arbol.insert('', 'end', text="1", values=('Juan', '1234', 'info@hola.com'))
arbol.insert('', 'end', text="1", values=('Jorge', '1234', 'info@hola.com'))
arbol.insert('', 'end', text="1", values=('Julia', '1234', 'info@hola.com'))
arbol.insert('', 'end', text="1", values=('Jean', '1234', 'info@hola.com'))

arbol.pack()



