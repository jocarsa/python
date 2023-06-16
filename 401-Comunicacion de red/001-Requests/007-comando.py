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
        if len(textos) == 0:
            print("No tienes etiqueta title y está mal")
        else:
            print("Si tienes etiqueta title y está bien")
            print("Y la longitud de tu título es de: "+str(len(str(textos[0]))))

raiz = tk.Tk()
raiz.geometry("300x500")
raiz.title("Comprobador SEO")

miurl = tk.StringVar(raiz)

marco = tk.Frame(raiz)
marco.pack()

tk.Label(marco,text="Introduce la URL que quieres comprobar:").pack(pady=10)
tk.Entry(marco,textvariable=miurl,width=30).pack(pady=10)
tk.Button(marco,command=compruebaSEO,text="Comprobar").pack(pady=10)


raiz.mainloop()

        
