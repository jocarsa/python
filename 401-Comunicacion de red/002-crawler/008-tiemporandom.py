#pip install requests
#pip install bs4
#pip install lxml
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import sqlite3 as db
import sys
import re
import time
import random

conexion = db.connect("buscador.sqlite")
cursor = conexion.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS "webs" (
	"Identificador"	INTEGER,
	"titulo"	TEXT,
	"descripcion"	TEXT,
	"url"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
    );
''')

def compruebaEnlaces(url):
    urlstring = ""
    if not "http" in url:
        urlstring = "https://"+ url
    else:
        urlstring = url
    try:
        respuesta = requests.get(urlstring)
        respuesta.raise_for_status()
    except HTTPError as mierror:
        print(mierror)
    except Exception as errorpython:
        print(errorpython)
    else:
        try:
            respuesta.encoding ='utf-8'
            sopa = BeautifulSoup(respuesta.text,'lxml')
            textos = sopa.find_all("title")
            titulo = str(textos[0])
            textos = sopa.find_all("meta", {"name" : "description"}) 
            descripcion = str(textos[0])
            cadena = '''
                    INSERT INTO webs VALUES(
                        NULL,
                        "'''+titulo.replace('"',"'")+'''",
                        "'''+descripcion.replace('"',"'")+'''",
                        "'''+url.replace('"',"'")+'''"
                    )
                '''
            print(cadena)
            cursor.execute(cadena)
            conexion.commit()
            enlaces = sopa.find_all("a")
            print(enlaces)
            aleatorio =  random.sample( enlaces, len(enlaces) )
            print("barajo")
            print(aleatorio)
            for enlace in aleatorio:
                if "http" in str(enlace):
                    print(enlace['href'])
                    segundos = random.randint(2, 6)
                    time.sleep(segundos)
                    compruebaEnlaces(enlace['href'])
        except:
            print("Ha habido algun error")
                

               
compruebaEnlaces("https://elpais.com/")          





        
