#pip install matplotlib
import matplotlib.pyplot as plot
import random as rand

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

lenguajes = ['Python', 'C++', 'Java', 'PHP', 'Javascript']
posicion = [20,8,6,4,2]

colores = []
for i in range(0,50):
    rojo = rand.randint(0, 255)
    verde = rand.randint(0, 255)
    azul = rand.randint(0, 255)
    colores.append(rgb_to_hex(rojo, verde, azul))

plot.bar(lenguajes, posicion, align='center', color=colores)
plot.ylabel('Uso de lenguajes de programación')
plot.title('Lenguajes de programación')

plot.show()
