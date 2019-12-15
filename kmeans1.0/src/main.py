import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from funciones import asignarCentros, actu, imp, algorithm, cost
import sys
from sklearn.datasets import make_circles,load_iris
import random

pd.options.mode.chained_assignment = None
iteraciones = 5
testing = 500
if 'n_samples' in sys.argv:
    testing = int(input('ingresar numero de ejemplos: '))


#base de datos por default
x,y = make_circles(n_samples=testing,factor=0.99,noise=0.1)
y = x[:,1]*10
x = x[:,0]*10
db = "circle"
if 'iter' in sys.argv:
        iteraciones = int(input('ingresar numero de iteraciones: '))

if 'iris' in sys.argv:
    iris = load_iris()
    x = iris.data
    y = x[0:testing,1]
    x = x[0:testing,0]
    db = 'iris'

#x,y = make_circles(n_samples=testing,factor=0.99,noise=0.35)


#declaramos un diccionario con los puntos en x e y de manera random
puntos = pd.DataFrame({
    'x': x,
    'y': y,
})

# ventana de pyplot para mostrar el grafico 

if __name__ == '__main__':
    determination = []
    k_array= []
    for k in range(10):
        b = []
        k += 1
        k_array.append(k)
        for i in range(k):
            b.append(random.randint(0,(len(puntos['x'])-1)))
        print(len(puntos['x']))
        centroides = pd.DataFrame({i+1: [puntos['x'][b[i]],puntos['y'][b[i]]] for i in range (len(b))})
        ventana = plt.figure(figsize = (3,3))
        plt.scatter(puntos['x'],puntos['y'], color = 'k')
        colores = {1:'blue',2:'green',3:'red',4:'cyan',5:'purple',6:'yellow',7:'brown',8:'pink',9:'olive',10:'gray'}
        for i in centroides.keys():
            plt.scatter(*centroides[i], color=colores[i])

        plt.show()
        for i in range(6):
            puntos,centroides = algorithm(puntos,centroides,k,colores)
            print(puntos.head())
        cost_func = cost(puntos,centroides)
        determination.append(cost_func)
    ventana = plt.figure(figsize = (6,6))
    plt.plot(k_array,determination, marker='o', color='b', label='Square')
    plt.show()
    # k = cantidad de centroides Kvar = promedio de distancia de un punto a un centroide
    comparision = pd.DataFrame({'Kvar':k_array,'prom':determination})
    print(comparision)


