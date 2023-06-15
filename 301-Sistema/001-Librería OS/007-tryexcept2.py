import os

listado = os.listdir('../../fotos')
print(listado)

contador = 1
try:
    os.mkdir("../../fotos2/")
except:
    print("Ha habido algún error al crear la carpeta")

for archivo in listado:
    print(archivo)
    try:
        os.rename("../../fotos/"+archivo,"../../fotos2/"+str(contador)+".jpg")
    except:
        print("el archivo ya existía")
    contador += 1

