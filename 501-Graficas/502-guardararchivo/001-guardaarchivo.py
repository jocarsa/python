import requests

url = 'https://jocarsa.com/log/registros.csv'
contenido = requests.get(url, allow_redirects=True)

open('registros.csv', 'wb').write(contenido.content)
