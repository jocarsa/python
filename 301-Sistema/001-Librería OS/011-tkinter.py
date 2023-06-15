import tkinter as tk

raiz = tk.Tk()
raiz.geometry("300x300")
marco = tk.Frame()
marco.pack()

tk.Label(marco,text="Introduce la carpeta de origen").pack()

raiz.mainloop()

