from flask import Flask
app = Flask(__name__)

@app.route('/')
def inicio():
    return "Esta es la página principal"

@app.route('/sobremi')
def sobremi():
    return "Esta es la página sobre mi"

@app.route('/proyectos')
def proyectos():
    return "Esta es la página de proyectos"

@app.route('/contacto')
def contacto():
    return "Esta es la página de contacto"
