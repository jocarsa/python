from flask import Flask
from flask import request
from flask import render_template
import sqlite3 as db
import sys
app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/busca', methods=['GET', 'POST'])
def prueba():
    
    loquebusco = request.form.get('criterio')
    conexion = db.connect("buscador.sqlite")
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT * FROM webs WHERE titulo LIKE "%'''+loquebusco+'''%"
    ''')
    datos = cursor.fetchall()
    cadena = ""
    for i in datos:
        cadena += "<h3>"+i[1]+"</h3><h4>"+i[2]+"</h4><p>"+i[3]+"</p>"

    
    conexion.commit()
    return render_template("busca.html",contenido=cadena)
   
