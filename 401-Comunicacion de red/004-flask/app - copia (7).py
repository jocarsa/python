from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/busca', methods=['GET', 'POST'])
def prueba():
    loquebusco = request.form.get('criterio')
    return "Voy a buscar: "+loquebusco
   
