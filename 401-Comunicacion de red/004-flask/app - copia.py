from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    cadena = ""
    for i in range(0,10):
        cadena = cadena + '<h1>Hola mundo!</h1>'
    return cadena
