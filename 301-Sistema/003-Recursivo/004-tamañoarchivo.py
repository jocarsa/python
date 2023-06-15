import os
def listadoRecursivo(directorio):
    listado = os.listdir(directorio)
    for elemento in listado:
        ruta = (directorio+"/"+elemento)
        if os.path.isdir(ruta):
            print("es carpeta: "+ruta)
            listadoRecursivo(ruta)
        else:
            estadisticas = os.stat(ruta)
            kb = estadisticas.st_size / (1024)
            print("es archivo: "+ruta+" y pesa "+str(kb)+"KB")
            


listadoRecursivo("C:/Users/Admin/Desktop")
