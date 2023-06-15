import PIL.Image
import random
import os
import tkinter as tk
from tkinter import filedialog
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
    for archivo in listado:
        imagen = PIL.Image.open(carpetaorigen+"/"+archivo)

        print(imagen.size)
        anchura =imagen.size[0] 
        altura =imagen.size[1]
        print("anchura: "+str(anchura)+",altura: "+str(altura))
        pixeles = imagen.load()
        minimo = 10000000
        minimotupla = (0,0,0)
        maximo = 0
        maximotupla = (0,0,0)
        print(pixeles[0,0])
        for x in range(0,anchura):
            for y in range(0,altura):
                media = round((pixeles[x,y][0]+pixeles[x,y][1]+pixeles[x,y][2])/3)
                if media < minimo:
                    minimo = media
                    minimotupla = pixeles[x,y]
                if media > maximo:
                    maximo = media
                    maximotupla = pixeles[x,y]

        print("la tupla menor es de: ",minimotupla)
        print("el mínimo de: ",minimo)
        print("la tupla mayor es de: ",maximotupla)
        print("el máximo de: ",maximo)
        print("El rango teórico es de 0,255, el rango práctico es de:0,"+str(maximo-minimo))
        factor = 255/(maximo-minimo)
        print("el factor es de: "+str(factor))

        for x in range(0,anchura):
            for y in range(0,altura):
                rojo = round((pixeles[x,y][0]-minimo)*factor)
                verde = round((pixeles[x,y][1]-minimo)*factor)
                azul = round((pixeles[x,y][2]-minimo)*factor)
                pixeles[x,y] = (rojo,verde,azul)
        imagen.save(carpetadestino+"/"+archivo, quality=100)
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













