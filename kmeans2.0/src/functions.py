import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import make_circles, load_iris
import random
import time
from IPython.display import clear_output
#asigna a los puntos de los datos que poseemos un centroide con la operacion matematica sqrt((x-xc)^2 + (y -yc)^2)
def asignar(puntos,centroides,dim,colores):
    for i in centroides.keys():
        res = 0
        for c in range(dim):
            n = c+1
            x = (puntos['x'+str(n)]-centroides[i][c])**2
            res += x
        res = np.sqrt(res)
        puntos['p'+str(i)] = res
    puntos['cercano a'] = puntos.loc[:,[('p'+str(i)) for i in centroides.keys()]].idxmin(axis=1)
    puntos['color'] = puntos['cercano a'].map(lambda x: colores[int(x.lstrip('p'))])
    return puntos

# actualiza las posiciones de los centroides
def actu(puntos,centroides,dim):
    for i in centroides.keys():
        for x in range(dim):
            a = (puntos[puntos['cercano a']== ('p'+str(i))]['x'+str(x+1)])
            #b = (puntos[puntos['cercano a']== ('p'+str(i))]['x2'])
            #c = (puntos[puntos['cercano a']== ('p'+str(i))]['x3'])
            #d = (puntos[puntos['cercano a']== ('p'+str(i))]['x4'])
            centroides[i][x] = sum(a)/len(a)#,(sum(b)/len(b)),(sum(c)/len(c)),(sum(d)/len(d))
    return centroides

#calcula el promedio de las distancias de los puntos con respecto a su centroide correspondiente
def cost(puntos,centroides):
    for i in centroides.keys():
        min = np.mean(puntos[puntos['cercano a']==('p'+str(i))][('p'+str(i))])
    cost = np.mean(min)
    return cost