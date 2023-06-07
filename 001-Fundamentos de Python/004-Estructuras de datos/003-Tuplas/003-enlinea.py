coordenada = [45,56,78]
print(coordenada)
coordenadatupla = (45,56,78)
print(coordenadatupla)
print("Lo convierto en una lista")
listatemporal = list(coordenadatupla)
listatemporal[0] = 0
print(listatemporal)
nuevatupla = tuple(listatemporal)
print(nuevatupla)
