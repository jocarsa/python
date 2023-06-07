#pip install matplotlib
import matplotlib.pyplot as plot

paises = ['España', 'Argentina', 'Perú', 'Chile', 'Italia','Bolivia','Belgica']
datos = [11,2,4,8,10,5,7]
plot.bar(paises,datos)
plot.title("Demostración")
plot.show()
