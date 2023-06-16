from flask import Flask
from flask import request
from flask import render_template
import sqlite3 as db
import sys
from bs4 import BeautifulSoup
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
        soup = BeautifulSoup(i[1], 'html.parser')
        titulo = soup.title.string
        soup = BeautifulSoup(i[2], 'html.parser')
        meta_tag = soup.find('meta', {'name': 'description'})
        descripcion = meta_tag.get('content')
        cadena += "<h3>"+titulo+"</h3><h4>"+descripcion+"</h4><p><a href='"+i[3]+"'>"+i[3]+"</a></p>"

    
    conexion.commit()
    return render_template("busca.html",contenido=cadena)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
