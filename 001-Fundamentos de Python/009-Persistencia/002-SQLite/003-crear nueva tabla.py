import sqlite3 as db
import sys

conexion = db.connect("agenda.sqlite")
cursor = conexion.cursor()
cursor.execute('''
    CREATE TABLE "contactos" (
	"Identificador"	INTEGER,
	"nombre"	TEXT,
	"telefono"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
    );
''')
