import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from funciones import asignarCentros, actu, imp, algorithm
import sys

#iteraciones default
iteraciones = 10

#declaramos un diccionario con los puntos en x e y de manera random
x = np.random.randint(0,100,60)
y = np.random.randint(0,100,60)
puntos = pd.DataFrame({
    'x': x,
    'y': y,
})
k = 3
# Declaramos los centroides del algoritmo
centroides = pd.DataFrame({i+1: [np.random.randint(0,60),np.random.randint(0,60)] for i in range(k)})
# ventana de pyplot para mostrar el grafico 
ventana = plt.figure(figsize = (6,6))
plt.scatter(puntos['x'],puntos['y'], color = 'k')
plt.scatter(*centroides[1], color='red')
plt.scatter(*centroides[2], color='blue')
plt.scatter(*centroides[3], color='green')
plt.ylim(0,100)
plt.xlim(0,100)
plt.show()

if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) >> 1:
        iteraciones = int(sys.argv[1])
    algorithm(iteraciones,puntos,centroides,k)
    
