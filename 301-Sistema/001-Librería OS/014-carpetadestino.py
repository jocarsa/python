import tkinter as tk
from tkinter import filedialog

def selCarpetaOrigen():
    carpetaorigen = filedialog.askdirectory()
    print(carpetaorigen)
def selCarpetaDestino():
    carpetadestino = filedialog.askdirectory()
    print(carpetadestino)

raiz = tk.Tk()
raiz.geometry("300x300")
marco = tk.Frame()
marco.pack()

tk.Label(marco,text="Introduce la carpeta de origen").pack()
tk.Button(marco,text="Selecciona",command=selCarpetaOrigen).pack()
tk.Label(marco,text="Introduce la carpeta de destino").pack()
tk.Button(marco,text="Selecciona",command=selCarpetaDestino).pack()


raiz.mainloop()

