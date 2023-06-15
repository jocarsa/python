import tkinter as tk
from tkinter import filedialog

def selCarpetaOrigen():
    carpetaorigen = filedialog.askdirectory()
    print(carpetaorigen)

raiz = tk.Tk()
raiz.geometry("300x300")
marco = tk.Frame()
marco.pack()

tk.Label(marco,text="Introduce la carpeta de origen").pack()
tk.Button(marco,text="Selecciona",command=selCarpetaOrigen).pack()


raiz.mainloop()

