import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from funciones import asignarCentros, actu, imp, algorithm
import sys
from sklearn.datasets import make_circles

pd.options.mode.chained_assignment = None
iteraciones = 3
testing = 500
if 'n_samples' in sys.argv:
    testing = int(input('ingresar numero de ejemplos: '))

if 'iter' in sys.argv:
        iteraciones = int(input('ingresar numero de iteraciones: '))

x,y = make_circles(n_samples=testing,factor=0.99,noise=0.35)
y = x[:,1]*10
x = x[:,0]*10


#declaramos un diccionario con los puntos en x e y de manera random
puntos = pd.DataFrame({
    'x': x,
    'y': y,
})
k = 3
# Declaramos los centroides del algoritmo
centroides = pd.DataFrame({i+1: [np.random.randint(-10,10),np.random.randint(-10,10)] for i in range(k)})
# ventana de pyplot para mostrar el grafico 
ventana = plt.figure(figsize = (6,6))
plt.scatter(puntos['x'],puntos['y'], color = 'k')
plt.scatter(*centroides[1], color='red')
plt.scatter(*centroides[2], color='blue')
plt.scatter(*centroides[3], color='green')
plt.ylim(-20,20)
plt.xlim(-20,20)
plt.show()

if __name__ == '__main__':
    algorithm(iteraciones,puntos,centroides,k)
    
