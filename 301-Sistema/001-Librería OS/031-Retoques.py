import tkinter as tk
from tkinter import filedialog
import os
import PIL.Image
from tkinter import ttk
import locale
import csv
import time

carpetaorigen = ""
carpetadestino = ""

archivo = open("lang.csv", "r")
csv = csv.DictReader(archivo)
print(csv)
traducciones = []

def current_milli_time():
    return round(time.time() * 1000)
    
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
    cuentaarchivo = 1
    for archivo in listado:
        try:
            print(archivo)
            imagen = PIL.Image.open(carpetaorigen+"/"+archivo)
            datosexif = imagen._getexif()
            fecha = datosexif[36868]
            epoch = datosexif[306]
            imagen.close()
            nuevafecha = fecha.replace(" ","-").replace(":","_")
            try:
                os.rename(carpetaorigen+"/"+archivo,carpetadestino+"/"+nuevafecha+"-"+str(current_milli_time())+".jpg")
            except Exception as error:
                print(error)
            dondeestoy = round((contador/longitud)*100)
            print(dondeestoy)
            progreso.set(dondeestoy)
            contador += 1
            etiquetaresultado.config(text = traducciones[5]+" "+str(longitud))
        except:
            print("error")
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
tk.Label(marco,text=traducciones[2]).pack(pady=10)
tk.Button(marco,text=traducciones[3],image=fondoboton,borderwidth=0,command=selCarpetaDestino).pack(pady=10)
tk.Button(marco,text=traducciones[4],image=fondoboton2,borderwidth=0,command=iniciar).pack(pady=10)
barraprogreso = ttk.Progressbar(marco,variable=progreso)
barraprogreso.pack(pady=10)
etiquetaresultado = tk.Label(marco,text="")
etiquetaresultado.pack()


mimenu = tk.Menu(raiz)
raiz.config(menu=mimenu)
mimenu.add_cascade(label="Ayuda",command=ayuda)

raiz.mainloop()

