import tkinter as interfaz

raiz = interfaz.Tk()
raiz.geometry("600x600+50+50")
raiz.title("Programa de Jose Vicente Carratalá")
raiz.iconbitmap("icono.ico")

panel = interfaz.Frame()
panel.pack()

etiqueta = interfaz.Label(panel,text="Hola mundo")
etiqueta.pack()

raiz.mainloop()
