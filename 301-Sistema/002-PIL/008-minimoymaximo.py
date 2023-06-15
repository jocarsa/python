import PIL.Image
import random

imagen = PIL.Image.open("naturaleza.jpg")

print(imagen.size)
anchura =imagen.size[0] 
altura =imagen.size[1]
print("anchura: "+str(anchura)+",altura: "+str(altura))
pixeles = imagen.load()
minimo = 10000000
minimotupla = (0,0,0)
print(pixeles[0,0])
for x in range(0,anchura):
    for y in range(0,altura):
        media = round((pixeles[x,y][0]+pixeles[x,y][1]+pixeles[x,y][2])/3)
        if media < minimo:
            minimo = media
            minimotupla = pixeles[x,y]

print("la tupla menor es de: ",minimotupla)
