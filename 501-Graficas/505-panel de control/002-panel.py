import requests
import sqlite3
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np


#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plot.subplot(2, 2, 1)
plot.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plot.subplot(2, 2, 2)
plot.plot(x,y)

#plot 3:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plot.subplot(2, 2, 3)
plot.plot(x,y)

#plot 4:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plot.subplot(2, 2, 4)
plot.plot(x,y)

plot.show()
