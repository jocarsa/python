import tkinter as interfaz

def nuevo():
    print("Voy a crear un nuevo registro")
def ver():
    print("Voy a ver registros")
def actualizar():
    print("Voy a actualizar un registro")
def eliminar():
    print("Voy a eliminar un registro")

#Ventana
raiz = interfaz.Tk()
raiz.geometry("600x600+50+50")
raiz.title("Agenda")
raiz.iconbitmap("icono.ico")

#Menu
mimenu = interfaz.Menu(raiz)
raiz.config(menu=mimenu)
menuagenda = interfaz.Menu(mimenu)
menuagenda.add_command(label="Crear",command=nuevo)
menuagenda.add_command(label="Ver",command=ver)
menuagenda.add_command(label="Actualizar",command=actualizar)
menuagenda.add_command(label="Eliminar",command=eliminar)


mimenu.add_cascade(label="Archivo")
mimenu.add_cascade(label="Agenda",menu=menuagenda)
mimenu.add_cascade(label="Ayuda")
