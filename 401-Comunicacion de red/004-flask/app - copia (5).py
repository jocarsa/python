from flask import Flask
from flask import request
app = Flask(__name__)

cabecera = '''
<!doctype html>
<html>
<head>
</head>
<body>
<h1>Buscador</h1>

<form method="POST" action="prueba">
    <input type="text" name="busca">
    <input type="submit">
</form>
'''

@app.route('/')
def inicio():
    return cabecera+"Esta es la página principal"



@app.route('/prueba', methods=['GET', 'POST'])
def prueba():
    loquebusco = request.form.get('busca')
    return "Voy a buscar: "+loquebusco
   
