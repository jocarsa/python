import sqlite3 as db
import sys

conexion = db.connect("agenda.sqlite")
cursor = conexion.cursor()
cursor.execute('''
    DELETE FROM
    contactos
    WHERE Identificador = 1
''')
conexion.commit()
