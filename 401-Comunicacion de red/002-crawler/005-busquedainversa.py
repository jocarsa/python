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
        for enlace in reversed(enlaces):
            if "http" in str(enlace):
                print(enlace['href'])
                time.sleep(5)
                compruebaEnlaces(enlace['href'])
                

               
compruebaEnlaces("https://escuelamastermedia.es/")          





        
