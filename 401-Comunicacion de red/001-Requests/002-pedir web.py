#pip install requests
import requests

with requests.Session() as misesion:
    pagina = misesion.get("https://jocarsa.com")
    print(pagina.content)
