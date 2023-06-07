# Programa agenda (c) 2023 Jose Vicente Carratala
print("Programa agenda")
print('''
    Selecciona una opción:
    1.-Crear registro
    2.-Listar registros
    3.-Actualizar registros
    4.-Eliminar registros
''')
opcion = input()
print("La opción que has seleccionado es: "+opcion)

if opcion == "1":
    print("Insertamos un nuevo registro")
elif opcion == "2":
    print("Listado de registros")
elif opcion == "3":
    print("Actualización de un registro")
elif opcion == "4":
    print("Eliminación de registros")
