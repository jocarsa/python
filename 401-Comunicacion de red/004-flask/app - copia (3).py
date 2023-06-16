from flask import Flask
app = Flask(__name__)

cabecera = '''
<!doctype html>
<html>
<head>
</head>
<body>
<h1>La web de Jose Vicente</h1>
<nav>
<ul>
    <li><a href="/">Inicio</a></li>
    <li><a href="/sobremi">Sobre mi</a></li>
    <li><a href="/proyectos">Proyectos</a></li>
    <li><a href="/contacto">Contacto</a></li>
</ul>
</nav>
'''

@app.route('/')
def inicio():
    return cabecera+"Esta es la página principal"

@app.route('/sobremi')
def sobremi():
    return cabecera+"Esta es la página sobre mi"

@app.route('/proyectos')
def proyectos():
    return cabecera+"Esta es la página de proyectos"

@app.route('/contacto')
def contacto():
    return cabecera+"Esta es la página de contacto"
