import sqlite3 as db
import sys

conexion = db.connect("agenda.sqlite")
cursor = conexion.cursor()
cursor.execute('''
    INSERT INTO contactos VALUES (
    NULL,
    "Jose Vicente",
    "1234",
    "info@josevicentecarratala.com"
    )
''')
conexion.commit()
