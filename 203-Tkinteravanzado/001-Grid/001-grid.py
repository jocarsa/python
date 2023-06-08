import tkinter as interfaz

raiz = interfaz.Tk()
raiz.geometry("600x600")

rejilla = interfaz.Frame()
rejilla.pack()


etiqueta4 = interfaz.Label(rejilla,text=" Arriba Izquierda")
etiqueta4.grid(row=0,column=0)

etiqueta5 = interfaz.Label(rejilla,text="Arriba Centro")
etiqueta5.grid(row=0,column=1)

etiqueta6 = interfaz.Label(rejilla,text="Arriba Derecha")
etiqueta6.grid(row=0,column=2)

etiqueta1 = interfaz.Label(rejilla,text="Izquierda")
etiqueta1.grid(row=1,column=0)

etiqueta2 = interfaz.Label(rejilla,text="Centro")
etiqueta2.grid(row=1,column=1)

etiqueta3 = interfaz.Label(rejilla,text="Derecha")
etiqueta3.grid(row=1,column=2)

etiqueta7 = interfaz.Label(rejilla,text="Abajo Izquierda")
etiqueta7.grid(row=2,column=0)

etiqueta8 = interfaz.Label(rejilla,text="Abajo Centro")
etiqueta8.grid(row=2,column=1)

etiqueta9 = interfaz.Label(rejilla,text="Abajo Derecha")
etiqueta9.grid(row=2,column=2)

