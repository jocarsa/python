import sqlite3 as db
import sys

conexion = db.connect("agenda.sqlite")
cursor = conexion.cursor()
cursor.execute('''
    SELECT * FROM contactos
''')
datos = cursor.fetchall()

for i in datos:
    print("Identificador:",i[0],"\t nombre:",i[1],"\t telefono: ",i[2],"\t email:",i[3])

conexion.commit()
