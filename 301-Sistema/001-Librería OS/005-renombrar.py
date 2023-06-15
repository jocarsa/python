import os

listado = os.listdir('../../fotos')
print(listado)

contador = 1
os.mkdir("../../fotos2/")

for archivo in listado:
    print(archivo)

    os.rename("../../fotos/"+archivo,"../../fotos2/"+str(contador)+".jpg")
    contador += 1

