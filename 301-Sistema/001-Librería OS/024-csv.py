import csv

archivo = open("lang.csv", "r")
csv = csv.DictReader(archivo)
print(csv)
traducciones = []
for linea in csv:
    traducciones.append(linea)
print(traducciones)
