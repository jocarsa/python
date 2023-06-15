import tkinter as tk
from tkinter import filedialog
import os
import PIL.Image
from tkinter import ttk
import locale
import csv

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
    listado = os.listdir(carpetaorigen)
    print(listado)
    longitud = len(listado)
    contador = 1
    for archivo in listado:
        print(archivo)
        imagen = PIL.Image.open(carpetaorigen+"/"+archivo)
        datosexif = imagen._getexif()
        fecha = datosexif[36868]
        imagen.close()
        nuevafecha = fecha.replace(" ","-").replace(":","_")
        try:
            os.rename(carpetaorigen+"/"+archivo,carpetadestino+"/"+nuevafecha+".jpg")
        except:
            print("el archivo ya existía")
        dondeestoy = round((contador/longitud)*100)
        print(dondeestoy)
        progreso.set(dondeestoy)
        contador += 1
        etiquetaresultado.config(text = traducciones[5]+" "+str(longitud))

    
raiz = tk.Tk()
raiz.geometry("300x300")
raiz.title("EXIF Renamer")
raiz.iconbitmap("logocamara.ico")
progreso = tk.IntVar()
marco = tk.Frame()
marco.pack()

tk.Label(marco,text=traducciones[0]).pack()
tk.Button(marco,text=traducciones[1],command=selCarpetaOrigen).pack()
tk.Label(marco,text=traducciones[2]).pack()
tk.Button(marco,text=traducciones[3],command=selCarpetaDestino).pack()
tk.Button(marco,text=traducciones[4],command=iniciar).pack()
barraprogreso = ttk.Progressbar(variable=progreso)
barraprogreso.pack()
etiquetaresultado = tk.Label(marco,text="")
etiquetaresultado.pack()
raiz.mainloop()

