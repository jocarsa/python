import tkinter as tk
from tkinter import filedialog

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
    print("vamos a ejecutar el programa")
    print("la carpeta de origen es: "+carpetaorigen)
    print("la carpeta de destino es: "+carpetadestino)
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

