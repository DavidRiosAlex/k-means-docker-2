import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import make_circles, load_iris
import random
import time
from IPython.display import clear_output
import sys
from functions import actu,asignar,cost
pd.options.mode.chained_assignment = None

colores = {1:'blue',2:'green',3:'red',4:'cyan',5:'purple',6:'yellow',7:'brown',8:'pink',9:'olive',10:'gray'}

n= 500
p = 2
iter = 10
k = 3
n_samples = 500
centr = 3
# por default hace circulos
if 'n_samples' in sys.argv:
    n_samples = int(input("Ingresar la cantidad de ejemplos a usar: "))
x,y= make_circles(n_samples=n_samples,factor=0.99,noise=0.05)

# agregando iris al comando que ejecuta el script, cambia la base de datos por defectos por iris. 
if 'iris' in sys.argv:
    iris = load_iris()
    x = iris.data
    x = x[:n_samples,:]
if 'iter' in sys.argv:
    iter = int(input("Ingresar la cantidad de iteraciones a usar: "))
if 'k' in sys.argv:
    centr = int(input("Ingresar la cantidad maxima de centroides a utilizar: "))
puntos = pd.DataFrame({})
distortion = []
k_array = []


if __name__ == "__main__":
    for k in range(centr):
        k += 1

        #crea un array donde se almacenara cuales fueron los k usados en el proyecto
        k_array.append(k)
        m,dim = x.shape
        puntos = pd.DataFrame({})
        for i in range(dim):
            puntos['x'+str(i+1)] = x[:,i]
        b = []

        #crea un array b, los valores en b seran iguales a una posicion de los puntos en el dataframe "puntos"
        #luego crea el dataframe centroides, que realizara k centroides que tomaran la posicion de un punto en el
        #dataframe "puntos"
        for i in range(k):
            b.append(random.randint(0,len(puntos['x1'])-1))
        centroides = pd.DataFrame({i+1: [puntos['x'+str(q+1)][b[i]] for q in range(dim)] for i in range (len(b))}) 

        #iteraciones por cantidad de centroides 
        for i in range(iter):

            # ejecutamos las funciones creadas en functions.py (./functions.py)

            puntos = asignar(puntos,centroides,dim,colores)
            centroides = actu(puntos,centroides,dim)

            #se grafica 
            figure = plt.figure(figsize=[6,6])
            plt.scatter(puntos['x1'], puntos['x2'], color=puntos['color'], alpha=0.8, edgecolor='k')
            plt.show()

        # tercera funcion de functions.py

        cost_func = cost(puntos,centroides)
        distortion.append(cost_func)

    figure = plt.figure(figsize=[6,6])
    plt.scatter(puntos['x1'], puntos['x2'], color=puntos['color'], alpha=0.8, edgecolor='k')
    plt.show()
    figure = plt.figure(figsize=[6,6])
    plt.plot(k_array, distortion, marker='o', linestyle='--', color='b', label='Square') 
    plt.xlabel("k")
    plt.ylabel("distortion")
    plt.show()
    print("dataframe final: ")
    print(puntos.head())
    print("distortion : ", distortion)
