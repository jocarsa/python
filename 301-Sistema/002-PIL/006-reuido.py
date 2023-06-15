import PIL.Image
import random

imagen = PIL.Image.open("josevicente.jpg")

print(imagen.size)
anchura =imagen.size[0] 
altura =imagen.size[1]
print("anchura: "+str(anchura)+",altura: "+str(altura))
pixeles = imagen.load()
print(pixeles[0,0])
for x in range(0,anchura):
    for y in range(0,altura):
        #print(pixeles[x,y])
        pixeles[x,y] = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
            )

imagen.save("josevicente2.jpg")
