import os
import PIL.Image

listado = os.listdir('../../fotos')
print(listado)

contador = 1
try:
    os.mkdir("../../fotos2/")
except:
    print("Ha habido algún error al crear la carpeta")

for archivo in listado:
    print(archivo)
    imagen = PIL.Image.open('../../fotos/'+archivo)
    datosexif = imagen._getexif()
    fecha = datosexif[36868]
    imagen.close()
    nuevafecha = fecha.replace(" ","-").replace(":","_")
    try:
        os.rename("../../fotos/"+archivo,"../../fotos2/"+nuevafecha+".jpg")
    except:
        print("el archivo ya existía")
    contador += 1

