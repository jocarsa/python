import PIL.Image
import random
import os

listado = os.listdir("../../naturaleza")
for archivo in listado:
    imagen = PIL.Image.open("../../naturaleza/"+archivo)

    print(imagen.size)
    anchura =imagen.size[0] 
    altura =imagen.size[1]
    print("anchura: "+str(anchura)+",altura: "+str(altura))
    pixeles = imagen.load()
    minimo = 10000000
    minimotupla = (0,0,0)
    maximo = 0
    maximotupla = (0,0,0)
    print(pixeles[0,0])
    for x in range(0,anchura):
        for y in range(0,altura):
            media = round((pixeles[x,y][0]+pixeles[x,y][1]+pixeles[x,y][2])/3)
            if media < minimo:
                minimo = media
                minimotupla = pixeles[x,y]
            if media > maximo:
                maximo = media
                maximotupla = pixeles[x,y]

    print("la tupla menor es de: ",minimotupla)
    print("el mínimo de: ",minimo)
    print("la tupla mayor es de: ",maximotupla)
    print("el máximo de: ",maximo)
    print("El rango teórico es de 0,255, el rango práctico es de:0,"+str(maximo-minimo))
    factor = 255/(maximo-minimo)
    print("el factor es de: "+str(factor))

    for x in range(0,anchura):
        for y in range(0,altura):
            rojo = round((pixeles[x,y][0]-minimo)*factor)
            verde = round((pixeles[x,y][1]-minimo)*factor)
            azul = round((pixeles[x,y][2]-minimo)*factor)
            pixeles[x,y] = (rojo,verde,azul)
    imagen.save("../../naturaleza2/"+archivo, quality=100)











