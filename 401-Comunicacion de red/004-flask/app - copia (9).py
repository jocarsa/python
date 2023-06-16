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
    
    for i in datos:
        print("Identificador:",i[0],"\n titulo:",i[1],"\n descripcion: ",i[2],"\n url:",i[3])
    
    conexion.commit()
    return render_template("busca.html",contenido="variable que viene desde Python")
   
