import tkinter as interfaz
from tkinter import ttk
import sqlite3 as db
import sys

conexion = db.connect("agenda.sqlite")
cursor = conexion.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS "contactos" (
	"Identificador"	INTEGER,
	"nombre"	TEXT,
	"telefono"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
    );
''')



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
    cursor.execute('''
        SELECT * FROM contactos
    ''')
    datos = cursor.fetchall()
    for item in arbol.get_children():
        arbol.delete(item)
    for i in datos:
        print('''
            Identificador:'''+str(i[0])+'''###############
            nombre:'''+str(i[1])+'''
            telefono: '''+str(i[2])+'''
            email:'''+str(i[3])+'''

            ''')
        arbol.insert('', 'end', text="1", values=(str(i[1]), str(i[2]), str(i[3])))
        
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
def operacioninsertar():
    print("Inserto en la base de datos")
    tomanuevonombre = nuevonombre.get()
    tomanuevotelefono = nuevotelefono.get()
    tomanuevoemail = nuevoemail.get()
    print("Voy a insertar el nombre:"+tomanuevonombre)
    print("Voy a insertar el telefono:"+tomanuevotelefono)
    print("Voy a insertar el email:"+tomanuevoemail)
    cursor.execute('''
        INSERT INTO contactos VALUES (
        NULL,
        "'''+tomanuevonombre+'''",
        "'''+tomanuevotelefono+'''",
        "'''+tomanuevoemail+'''"
        )
    ''')
    conexion.commit()
    camponuevonombre.delete(0, interfaz.END)
    camponuevotelefono.delete(0, interfaz.END)
    camponuevoemail.delete(0, interfaz.END)

def operacioneliminar():
    print("Elimino en la base de datos")
    tomaidliminar = ideliminar.get()
    cursor.execute('''
        DELETE FROM contactos WHERE Identificador = '''+tomaidliminar+'''
    ''')
    conexion.commit()
    campoideliminar.delete(0, interfaz.END)
    

#Ventana
raiz = interfaz.Tk()
raiz.geometry("600x600+50+50")
raiz.title("Agenda")
raiz.iconbitmap("icono.ico")
raiz.configure('Treeview', rowheight=40)

#Variables de formulario
nuevonombre = interfaz.StringVar(raiz)
nuevotelefono = interfaz.StringVar(raiz)
nuevoemail = interfaz.StringVar(raiz)
ideliminar = interfaz.StringVar(raiz)

#Marcos

marcocrear = interfaz.Frame(raiz)
interfaz.Label(marcocrear,text="Creación de un nuevo registro").pack(pady=5)
interfaz.Label(marcocrear,text="Introduce el nombre").pack(pady=5)
camponuevonombre = interfaz.Entry(marcocrear,textvariable=nuevonombre,width=40)
camponuevonombre.pack(pady=5)
interfaz.Label(marcocrear,text="Introduce el telefono").pack(pady=5)
camponuevotelefono = interfaz.Entry(marcocrear,textvariable=nuevotelefono,width=40)
camponuevotelefono.pack(pady=5)
interfaz.Label(marcocrear,text="Introduce el email").pack(pady=5)
camponuevoemail = interfaz.Entry(marcocrear,textvariable=nuevoemail,width=40)
camponuevoemail.pack(pady=5)
interfaz.Button(marcocrear,text="Inserta nuevo registro",width=40,command=operacioninsertar).pack(pady=5)
print(camponuevonombre)

marcover = interfaz.Frame(raiz)
interfaz.Label(marcover,text="Listado de registros").pack()
arbol = ttk.Treeview(marcover, column=("Nombre", "Telefono", "Email"), show='headings', height=5)
arbol.column("# 1", anchor=interfaz.CENTER)
arbol.heading("# 1", text="Nombre")
arbol.column("# 2", anchor=interfaz.CENTER)
arbol.heading("# 2", text="Telefono")
arbol.column("# 3", anchor=interfaz.CENTER)
arbol.heading("# 3", text="Email")
arbol.pack()


marcoactualizar = interfaz.Frame(raiz)
interfaz.Label(marcoactualizar,text="Actualización de un registro").pack()

marcoeliminar = interfaz.Frame(raiz)
interfaz.Label(marcoeliminar,text="Eliminación de un registro").pack()
interfaz.Label(marcoeliminar,text="Introduce el id a eliminar").pack(pady=5)
campoideliminar = interfaz.Entry(marcoeliminar,textvariable=ideliminar,width=40)
campoideliminar.pack(pady=5)
interfaz.Button(marcoeliminar,text="Eliminar registro",width=40,command=operacioneliminar).pack(pady=5)

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
