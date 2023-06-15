import os
import sqlite3 as db
import sys
conexion = db.connect("disco2.sqlite")
cursor = conexion.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS "elementos" (
	"Identificador"	INTEGER,
	"ruta"	TEXT,
	"tamanio"	NUMERIC,
	"tipo"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
    );
''')
def listadoRecursivo(directorio):
    listado = os.listdir(directorio)
    for elemento in listado:
        ruta = (directorio+"/"+elemento)
        if os.path.isdir(ruta):
            print("es carpeta: "+ruta)
            listadoRecursivo(ruta)
            cursor.execute('''
                INSERT INTO elementos VALUES(
                    NULL,
                    "'''+ruta+'''",
                    "0",
                    "carpeta"
                )
            ''')
            conexion.commit()
        else:
            estadisticas = os.stat(ruta)
            kb = estadisticas.st_size / (1024)
            print("es archivo: "+ruta+" y pesa "+str(kb)+"KB")
            cursor.execute('''
                INSERT INTO elementos VALUES(
                    NULL,
                    "'''+ruta+'''",
                    '''+str(kb)+''',
                    "archivo"
                )
            ''')
            conexion.commit()


listadoRecursivo("C:/Users/Admin/Desktop")
