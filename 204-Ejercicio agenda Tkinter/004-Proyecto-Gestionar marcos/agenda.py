import tkinter as interfaz

def nuevo():
    print("Voy a crear un nuevo registro")
    marcoinicio.pack_forget()
    marcocrear.pack()
    marcover.pack_forget()
    marcoactualizar.pack_forget()
    marcoeliminar.pack_forget()
def ver():
    print("Voy a ver registros")
    marcoinicio.pack_forget()
    marcocrear.pack_forget()
    marcover.pack()
    marcoactualizar.pack_forget()
    marcoeliminar.pack_forget()
def actualizar():
    print("Voy a actualizar un registro")
    marcoinicio.pack_forget()
    marcocrear.pack_forget()
    marcover.pack_forget()
    marcoactualizar.pack()
    marcoeliminar.pack_forget()
def eliminar():
    print("Voy a eliminar un registro")
    marcoinicio.pack_forget()
    marcocrear.pack_forget()
    marcover.pack_forget()
    marcoactualizar.pack_forget()
    marcoeliminar.pack()

#Ventana
raiz = interfaz.Tk()
raiz.geometry("600x600+50+50")
raiz.title("Agenda")
raiz.iconbitmap("icono.ico")

#Marcos
marcocrear = interfaz.Frame(raiz)
interfaz.Label(marcocrear,text="Creación de un nuevo registro").pack()
marcover = interfaz.Frame(raiz)
interfaz.Label(marcover,text="Listado de registros").pack()
marcoactualizar = interfaz.Frame(raiz)
interfaz.Label(marcoactualizar,text="Actualización de un registro").pack()
marcoeliminar = interfaz.Frame(raiz)
interfaz.Label(marcoeliminar,text="Eliminación de un registro").pack()
marcoinicio = interfaz.Frame(raiz)
marcoinicio.pack()

#Marco de inicio
interfaz.Label(marcoinicio,text="Programa agenda").pack()
interfaz.Label(marcoinicio,text="(c) 2023 Jose Vicente Carratala").pack()



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
