#pip install matplotlib
import matplotlib.pyplot as plot

lenguajes = ['Python', 'C++', 'Java', 'PHP', 'Javascript']
posicion = [20,8,6,4,2]

plot.bar(lenguajes, posicion, align='center', alpha=0.5)
plot.ylabel('Uso de lenguajes de programación')
plot.title('Lenguajes de programación')

plot.savefig("grafica.png")
