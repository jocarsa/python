#pip install matplotlib
import matplotlib.pyplot as plot

lenguajes = ['Python', 'C++', 'Java', 'PHP', 'Javascript']
posicion = [20,8,6,4,2]

plot.bar(lenguajes, posicion, align='center', color=['red', 'green', 'blue', 'yellow', 'cyan'])
plot.ylabel('Uso de lenguajes de programación')
plot.title('Lenguajes de programación')

plot.show()
