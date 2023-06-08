import tkinter as interfaz

def nuevo():
    print("Voy a crear un archivo nuevo")
    marcoabrir.pack_forget()
    marcoguardar.pack_forget()
    marcocerrar.pack_forget()
    marconuevo.pack()
def abrir():
    marcoabrir.pack()
    marcoguardar.pack_forget()
    marcocerrar.pack_forget()
    marconuevo.pack_forget()
    print("Voy a abrir un archivo")
def guardar():
    marcoabrir.pack_forget()
    marcoguardar.pack()
    marcocerrar.pack_forget()
    marconuevo.pack_forget()
    print("Voy a guardar un archivo")
def cerrar():
    marcoabrir.pack_forget()
    marcoguardar.pack_forget()
    marcocerrar.pack()
    marconuevo.pack_forget()
    print("Voy a cerrar un archivo")

raiz = interfaz.Tk()
raiz.geometry("300x300")

marconuevo = interfaz.Frame(raiz)
interfaz.Label(marconuevo,text="Soy el nuevo").pack()

marcoabrir = interfaz.Frame(raiz)
interfaz.Label(marcoabrir,text="Voy a abrir").pack()

marcoguardar = interfaz.Frame(raiz)
interfaz.Label(marcoguardar,text="Voy a guardar").pack()

marcocerrar = interfaz.Frame(raiz)
interfaz.Label(marcocerrar,text="Voy a cerrar").pack()



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





