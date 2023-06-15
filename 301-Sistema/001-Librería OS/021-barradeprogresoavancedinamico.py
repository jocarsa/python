import tkinter as tk
from tkinter import filedialog
import os
import PIL.Image
from tkinter import ttk

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

    
raiz = tk.Tk()
raiz.geometry("300x300")
progreso = tk.IntVar()
marco = tk.Frame()
marco.pack()

tk.Label(marco,text="Introduce la carpeta de origen").pack()
tk.Button(marco,text="Selecciona",command=selCarpetaOrigen).pack()
tk.Label(marco,text="Introduce la carpeta de destino").pack()
tk.Button(marco,text="Selecciona",command=selCarpetaDestino).pack()
tk.Button(marco,text="Vamos",command=iniciar).pack()
barraprogreso = ttk.Progressbar(variable=progreso)
barraprogreso.pack()
barraprogreso.step(0)
raiz.mainloop()

