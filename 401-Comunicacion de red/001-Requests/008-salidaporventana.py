#pip install requests
#pip install bs4
#pip install lxml
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import tkinter as tk

def compruebaSEO():
    try:
        respuesta = requests.get(miurl.get())
        respuesta.raise_for_status()
    except HTTPError as mierror:
        print(mierror)
    except Exception as errorpython:
        print(errorpython)
    else:
        respuesta.encoding ='utf-8'
        sopa = BeautifulSoup(respuesta.text,'lxml')
        textos = sopa.find_all("title")
        campodetexto.insert(tk.END, 'Comprobación de título\n')
        if len(textos) == 0:
            campodetexto.insert(tk.END, 'No se encuentra etiqueta de título\n')
        else:
            campodetexto.insert(tk.END, 'Se ha encontrado un título:\n')
            campodetexto.insert(tk.END, str(textos[0])+"\n")
            campodetexto.insert(tk.END, "Longitud del título: "+str(len(str(textos[0])))+"\n")         

raiz = tk.Tk()
raiz.geometry("600x800")
raiz.title("Comprobador SEO")

miurl = tk.StringVar(raiz)

marco = tk.Frame(raiz)
marco.pack()

tk.Label(marco,text="Introduce la URL que quieres comprobar:").pack(pady=10)
tk.Entry(marco,textvariable=miurl,width=30).pack(pady=10)
tk.Button(marco,command=compruebaSEO,text="Comprobar").pack(pady=10)
campodetexto = tk.Text(marco, height=40, width=70)
campodetexto.pack()


raiz.mainloop()

        
