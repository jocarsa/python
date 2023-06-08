import tkinter as interfaz

def nuevo():
    print("Voy a crear un archivo nuevo")
def abrir():
    print("Voy a abrir un archivo")
def guardar():
    print("Voy a guardar un archivo")
def cerrar():
    print("Voy a cerrar un archivo")

raiz = interfaz.Tk()
raiz.geometry("300x300")

marco = interfaz.Frame(raiz)
marco.pack()

mimenu = interfaz.Menu(raiz)

raiz.config(menu=mimenu)

menuarchivo = interfaz.Menu(mimenu)
menuarchivo.add_command(label="Nuevo",command=nuevo)
menuarchivo.add_command(label="Abrir",command=abrir)
menuarchivo.add_command(label="Guardar",command=guardar)
menuarchivo.add_command(label="Cerrar",command=cerrar)


mimenu.add_cascade(label="Archivo",menu=menuarchivo)
mimenu.add_cascade(label="Editar")
mimenu.add_cascade(label="Ayuda")





