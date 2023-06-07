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
        insertar()
    elif opcion == "2":
        leer()
    elif opcion == "3":
        actualizar()
    elif opcion == "4":
        eliminar()
    elif opcion == "5":
        salir()
        
    print("Operación finalizada, volvemos al menú:")
    menu()


def actualizar():
    print("Actualización de un registro")
    identificador = input("Introduce el registro que deseas actualizar: ")
    cursor.execute('''
        SELECT * FROM contactos
        WHERE Identificador = '''+identificador+'''
    ''')
    datos = cursor.fetchall()
    nombreanterior = ""
    telefonoanterior = ""
    correoanterior = ""
    for i in datos:
        nombreanterior = str(i[1])
        telefonoanterior = str(i[2])
        correoanterior = str(i[3])
        
    nombre = input("Introduce un nuevo nombre ("+nombreanterior+"):")
    telefono = input("Introduce un nuevo teléfono ("+telefonoanterior+"):")
    email = input("Introduce un nuevo email ("+correoanterior+"):")
    cursor.execute('''
        UPDATE contactos SET 
        
        nombre = "'''+nombre+'''",
        telefono = "'''+telefono+'''",
        email = "'''+email+'''"

        WHERE Identificador = '''+identificador+'''
    ''')
    conexion.commit()

def eliminar():
    print("Eliminación de registros")
    identificador = input("Selecciona el registro para eliminar: ")
    cursor.execute('''
        DELETE FROM
        contactos
        WHERE Identificador = '''+identificador+'''
    ''')
    conexion.commit()

def leer():
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

def salir():
    print("Saliendo del programa...")
    exit()

def insertar():
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


