import os
def listadoRecursivo(directorio):
    listado = os.listdir(directorio)
    for elemento in listado:
        ruta = (directorio+"/"+elemento)
        if os.path.isdir(ruta):
            print("es carpeta: "+ruta)
            listadoRecursivo(ruta)
        else:
            print("es archivo: "+ruta)


listadoRecursivo("C:\\Users\\Admin\\Desktop")
