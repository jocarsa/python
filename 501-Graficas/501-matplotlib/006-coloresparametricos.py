#pip install matplotlib
import matplotlib.pyplot as plot

lenguajes = ['Python', 'C++', 'Java', 'PHP', 'Javascript']
posicion = [20,8,6,4,2]

colores = ['#ff0000', '#00ff00', '#0000ff', 'yellow', 'cyan']

plot.bar(lenguajes, posicion, align='center', color=colores)
plot.ylabel('Uso de lenguajes de programación')
plot.title('Lenguajes de programación')

plot.show()
