#pip install requests
#pip install bs4
#pip install lxml
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

with requests.Session() as misesion:
    pagina = misesion.get("https://jocarsa.com")
    #print(pagina.content)
    
for direccion in ['https://jocarsa.com']:
    try:
        respuesta = requests.get(direccion)
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



        
