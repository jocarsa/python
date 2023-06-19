#pip install matplotlib
import matplotlib.pyplot as plot

numeros = [35, 25, 25, 15]
etiquetas = ["Python","C++","PHP","Javascript"]
plot.pie(numeros,labels = etiquetas)
plot.show() 
