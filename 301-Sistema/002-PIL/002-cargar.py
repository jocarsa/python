import PIL.Image

imagen = PIL.Image.open("josevicente.jpg")
print(imagen.size)
anchura =imagen.size[0] 
altura =imagen.size[1]
print("anchura: "+str(anchura)+",altura: "+str(altura))
