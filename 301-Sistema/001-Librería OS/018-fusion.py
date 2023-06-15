import tkinter as tk
from tkinter import filedialog
import os
import PIL.Image

carpetaorigen = ""
carpetadestino = ""

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

    
raiz = tk.Tk()
raiz.geometry("300x300")
marco = tk.Frame()
marco.pack()

tk.Label(marco,text="Introduce la carpeta de origen").pack()
tk.Button(marco,text="Selecciona",command=selCarpetaOrigen).pack()
tk.Label(marco,text="Introduce la carpeta de destino").pack()
tk.Button(marco,text="Selecciona",command=selCarpetaDestino).pack()
tk.Button(marco,text="Vamos",command=iniciar).pack()

raiz.mainloop()

