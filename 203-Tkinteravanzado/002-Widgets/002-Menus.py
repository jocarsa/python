import tkinter as interfaz

raiz = interfaz.Tk()
raiz.geometry("300x300")

marco = interfaz.Frame(raiz)
marco.pack()

mimenu = interfaz.Menu(raiz)

raiz.config(menu=mimenu)

menuarchivo = interfaz.Menu(mimenu)
menuarchivo.add_command(label="Nuevo")
menuarchivo.add_command(label="Abrir")
menuarchivo.add_command(label="Guardar")
menuarchivo.add_command(label="Cerrar")


mimenu.add_cascade(label="Archivo",menu=menuarchivo)
mimenu.add_cascade(label="Editar")
mimenu.add_cascade(label="Ayuda")





