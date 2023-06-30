#pip install requests
#pip install bs4
#pip install lxml
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import tkinter as tk
from tkinter import ttk
import operator
from collections import Counter
import re



def compruebaSEO():
    urlstring = ""
    if not "http" in miurl.get():
        urlstring = "https://"+ miurl.get()
    else:
        urlstring = miurl.get()
    try:
        respuesta = requests.get(urlstring)
        respuesta.raise_for_status()
    except HTTPError as mierror:
        print(mierror)
    except Exception as errorpython:
        print(errorpython)
    else:
        respuesta.encoding ='utf-8'
        sopa = BeautifulSoup(respuesta.text,'lxml')
        # Búsqueda de título
        textos = sopa.find_all("title") 
        if len(textos) == 0:
            arbol.insert('', 'end', text="1", values=('ko', 'Titulo', 'No existe'))
        else:
            arbol.insert('', 'end', text="1", values=('ok', 'Titulo', str(textos[0])))
        # Búsqueda de descripción
        textos = sopa.find_all("meta", {"name" : "description"})
        if len(textos) == 0:
            arbol.insert('', 'end', text="1", values=('ko', 'Descripción', 'No existe'))          
        else:
            arbol.insert('', 'end', text="1", values=('ok', 'Descripción', str(textos[0])))
        #palabras mas repetidas
        spanish_stop_words = [
            "a", "al", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "e", "el", "en", "entre", "hacia", "hasta", "la",
            "las", "le", "les", "lo", "los", "me", "mi", "mis", "mía", "mías", "mío", "míos", "nada", "ni", "no", "nos", "nosotros",
            "nuestra", "nuestras", "nuestro", "nuestros", "o", "os", "otra", "otras", "otro", "otros", "para", "pero", "por", "que",
            "se", "si", "sin", "sobre", "sois", "somos", "son", "su", "sus", "tanto", "te", "tu", "tus", "tú", "un", "una", "uno",
            "unos", "vosotros", "vuestra", "vuestras", "vuestro", "vuestros", "y", "ya"
        ]
        text = sopa.get_text()
        processed_text = re.sub(r'\W+', ' ', text.lower())
        words = processed_text.split()
        words = [word for word in words if word not in spanish_stop_words and not word.isdigit()]
        word_counts = Counter(words)
        most_common = word_counts.most_common(5)
        cadena= ""
        for word, count in most_common:
            print(word, count)
            cadena+= word+":"+str(count)+" - "
        arbol.insert('', 'end', text="1", values=('ok', 'Palabras clave', cadena))

raiz = tk.Tk()
raiz.geometry("600x800")
raiz.title("Comprobador SEO")

miurl = tk.StringVar(raiz)

marco = tk.Frame(raiz)
marco.pack()

ok = tk.PhotoImage(file = "ok.png")
ko = tk.PhotoImage(file = "ko.png")

tk.Label(marco,text="Introduce la URL que quieres comprobar:").pack(pady=10)
entrada = tk.Entry(marco,textvariable=miurl,width=30)
entrada.pack(pady=10)
entrada.insert(0, "https://jocarsa.com")
tk.Button(marco,command=compruebaSEO,text="Comprobar").pack(pady=10)
#campodetexto = tk.Text(marco, height=1, width=4,font="Arial 10")
arbol = ttk.Treeview(raiz, column=("Nombre", "Telefono", "Email"), show='headings', height=50)
arbol.column("# 1", anchor=tk.CENTER,width=10)
arbol.heading("# 1", text="Resultado")
arbol.column("# 2", anchor=tk.CENTER,width=200)
arbol.heading("# 2", text="Marcador")
arbol.column("# 3", anchor=tk.CENTER,width=400)
arbol.heading("# 3", text="Comentario")
arbol.tag_configure("left_align", anchor="w")

arbol.pack()

raiz.mainloop()

        
