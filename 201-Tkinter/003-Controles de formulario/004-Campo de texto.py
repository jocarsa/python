import tkinter as interfaz

raiz = interfaz.Tk()
raiz.geometry("600x600+50+50")
raiz.title("Programa de Jose Vicente Carratalá")
raiz.iconbitmap("icono.ico")

panel = interfaz.Frame()
panel.pack()

etiqueta = interfaz.Label(panel,text="Hola mundo",fg="red",bg="blue",font=("Arial",25))
etiqueta.pack()

campo = interfaz.Entry(panel)
campo.pack()

raiz.mainloop()
