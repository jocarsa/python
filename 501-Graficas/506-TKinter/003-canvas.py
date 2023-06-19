import tkinter as tk

raiz = tk.Tk()
raiz.geometry("512x512")
lienzo = tk.Canvas()
lienzo.pack()
lienzo.create_rectangle(10,10,20,20,fill="red")
lienzo.create_rectangle(50,50,70,70,fill="blue")
raiz.mainloop()
