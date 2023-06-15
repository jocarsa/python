import tkinter as tk
from tkinter import filedialog

raiz = tk.Tk()
raiz.geometry("300x300")
marco = tk.Frame()
marco.pack()

tk.Label(marco,text="Introduce la carpeta de origen").pack()
folder_selected = filedialog.askdirectory()

raiz.mainloop()

