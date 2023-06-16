#pip install requests
#pip install bs4
#pip install lxml
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError


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

               
compruebaEnlaces("https://jocarsa.com")          





        
