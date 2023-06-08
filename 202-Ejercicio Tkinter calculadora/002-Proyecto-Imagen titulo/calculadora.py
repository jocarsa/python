import tkinter as interfaz

raiz = interfaz.Tk()
raiz.geometry("600x600+50+50")
raiz.title("Calculadora Freelance")
raiz.iconbitmap("icono.ico")

panel = interfaz.Frame()
panel.pack()

imagen = interfaz.PhotoImage(file="titulo.png")
etiquetaimagen = interfaz.Label(raiz, image=imagen)
etiquetaimagen.pack()
