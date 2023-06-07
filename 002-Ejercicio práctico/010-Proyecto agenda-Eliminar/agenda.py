# Programa agenda (c) 2023 Jose Vicente Carratala

import sqlite3 as db
import sys

conexion = db.connect("agenda.sqlite")
cursor = conexion.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS "contactos" (
	"Identificador"	INTEGER,
	"nombre"	TEXT,
	"telefono"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
    );
''')

print("Programa agenda")
def menu():
    print('''
        Selecciona una opción:
        1.-Crear registro
        2.-Listar registros
        3.-Actualizar registros
        4.-Eliminar registros
        5.-Salir del programa
    ''')
    opcion = input()
    print("La opción que has seleccionado es: "+opcion)

    if opcion == "1":
        print("Insertamos un nuevo registro")
        nombre = input("Introduce un nuevo nombre:")
        telefono = input("Introduce un nuevo teléfono:")
        email = input("Introduce un nuevo email:")
        cursor.execute('''
            INSERT INTO contactos VALUES (
            NULL,
            "'''+nombre+'''",
            "'''+telefono+'''",
            "'''+email+'''"
            )
        ''')
        conexion.commit()
    elif opcion == "2":
        print("Listado de registros")
        cursor.execute('''
            SELECT * FROM contactos
        ''')
        datos = cursor.fetchall()

        for i in datos:
            print('''
                Identificador:'''+str(i[0])+'''###############
                nombre:'''+str(i[1])+'''
                telefono: '''+str(i[2])+'''
                email:'''+str(i[3])+'''

                ''')
    elif opcion == "3":
        print("Actualización de un registro")
    elif opcion == "4":
        print("Eliminación de registros")
        identificador = input("Selecciona el registro para eliminar")
        cursor.execute('''
            DELETE FROM
            contactos
            WHERE Identificador = '''+identificador+'''
        ''')
        conexion.commit()
    elif opcion == "5":
        print("Saliendo del programa...")
        exit()
        
    print("Operación finalizada, volvemos al menú:")
    menu()

menu()
