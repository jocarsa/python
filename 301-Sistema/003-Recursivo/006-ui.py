import os
import sqlite3 as db
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import locale
import csv

conexion = db.connect("disco2.sqlite")
cursor = conexion.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS "elementos" (
	"Identificador"	INTEGER,
	"ruta"	TEXT,
	"tamanio"	NUMERIC,
	"tipo"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
    );
''')

carpetaorigen = ""
carpetadestino = ""

archivo = open("lang.csv", "r")
csv = csv.DictReader(archivo)
print(csv)
traducciones = []


    
print(traducciones)
idioma = locale.getdefaultlocale()[0]
print("El idioma de tu ordenador es:"+idioma)
idiomaapp = "es"
for linea in csv:
    if "es" in idioma:
        traducciones.append(linea['es'])

    else:
        traducciones.append(linea['en'])
print(traducciones)


def selCarpetaOrigen():
    global carpetaorigen
    carpetaorigen = filedialog.askdirectory()
    print(carpetaorigen)
def selCarpetaDestino():
    global carpetadestino
    carpetadestino = filedialog.askdirectory()
    print(carpetadestino)
def iniciar():
    listadoRecursivo(carpetaorigen)
def ayuda():
    print("vamos a por la ayuda")
    tk.messagebox.showinfo(
        title="Instrucciones",
        message='''
        Renombrador de archivos JPG con información EXIF
        1.-Selecciona la carpeta de origen
        2.-Selecciona la carpeta de destino
        3.-Pulsa el botón verde para iniciar
        Y el sistema renombrará tus fotografías usando la información EXIF existente
        '''
    )
def listadoRecursivo(directorio):
    listado = os.listdir(directorio)
    for elemento in listado:
        ruta = (directorio+"/"+elemento)
        if os.path.isdir(ruta):
            print("es carpeta: "+ruta)
            listadoRecursivo(ruta)
            cursor.execute('''
                INSERT INTO elementos VALUES(
                    NULL,
                    "'''+ruta+'''",
                    "0",
                    "carpeta"
                )
            ''')
            conexion.commit()
        else:
            estadisticas = os.stat(ruta)
            kb = estadisticas.st_size / (1024)
            print("es archivo: "+ruta+" y pesa "+str(kb)+"KB")
            cursor.execute('''
                INSERT INTO elementos VALUES(
                    NULL,
                    "'''+ruta+'''",
                    '''+str(kb)+''',
                    "archivo"
                )
            ''')
            conexion.commit()
            
raiz = tk.Tk()
raiz.geometry("300x500")
raiz.title("EXIF Renamer")
raiz.iconbitmap("logocamara.ico")
progreso = tk.IntVar()
marco = tk.Frame()
marco.pack()
imagen = tk.PhotoImage(file="logocamara.png")
fondoboton= tk.PhotoImage(file='boton.png')
fondoboton2= tk.PhotoImage(file='boton2.png')
tk.Label(marco, image=imagen).pack()
tk.Label(marco, text="EXIF Renamer (c) 2023 Jose Vicente Carratalá").pack()
tk.Label(marco,text=traducciones[0]).pack(pady=10)
tk.Button(marco,text=traducciones[1],image=fondoboton,borderwidth=0,command=selCarpetaOrigen).pack(pady=10)

tk.Button(marco,text=traducciones[4],image=fondoboton2,borderwidth=0,command=iniciar).pack(pady=10)
barraprogreso = ttk.Progressbar(marco,variable=progreso)
barraprogreso.pack(pady=10)
etiquetaresultado = tk.Label(marco,text="")
etiquetaresultado.pack()


mimenu = tk.Menu(raiz)
raiz.config(menu=mimenu)
mimenu.add_cascade(label="Ayuda",command=ayuda)








