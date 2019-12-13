import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

#esta operacion asigna los centroides a una zona del eje de coordenadas
def asignarCentros(centroides,puntos,k,colores=['r','b','g']):
    for i in range(k):


        #se asigna los valores de las operaciones para x y para y
        x = ((puntos['x'] - centroides[i+1][0]) ** 2)
        y = (puntos['y'] - centroides[i+1][1]) ** 2


        #se saca la raiz cuadrada de la suma de los dos anteriores
        res = np.sqrt(x+y)


        #se crea (y si ya esta creada se asigna) la llave "distancia" a p con la vuelta i y a la misma se le da el
        #valor res 
        string = 'distancia a p'+str(i+1)
        puntos[string] = res

    #creamos un array que luego se agregara en el dataframe de puntos
    centroi_array = [('distancia a p'+str(i)) for i in centroides]

    # se crea la llave cercano, en referencia a los centroides cercanos a un punto
    #los almacena buscando el valor minimo entre los 3 puntos de distancia y agregando solamente el nombre de la
    #columna a la que corresponde
    puntos['cercano'] = puntos.loc[:, centroi_array].idxmin(axis=1)


    # a cercanos le quitamos la palabra "distancia a p" que correspondia a la columna
    # para que solo se almacene el numero correspondiente
    #al centroide cercano a este punto
    puntos['cercano'] = puntos['cercano'].map(lambda x: int(x.lstrip('distancia a p')))


    #se le asigna un color a cada punto correspondiente al conjunto de datos que pertenece a un centroide n
    #en el dataframe
    puntos['color'] = puntos['cercano'].map(lambda x: colores[x-1])


    #y se regresa el dataframe modificado 
    return puntos


def actu(centroides,puntos):
    for i in centroides.keys():
        #el centroide cambia de posicion segun el promedio de todos los puntos en x e y, que corresponden 
        # al centroide operando 
        centroides[i][0],centroides[i][1] = (np.mean(puntos[puntos['cercano']== i]['x']),
        np.mean(puntos[puntos['cercano']== i]['y']))


    return centroides


def imp(puntos,centroides):

    #graficacion
    ventana = plt.figure(1,figsize = (6,6))
    plt.scatter(puntos['x'], puntos['y'], color=puntos['color'], alpha=0.8, edgecolor='k')
    plt.scatter(*centroides[1], color='black')
    plt.scatter(*centroides[2], color='black')
    plt.scatter(*centroides[3], color='black')
    plt.ylim(0,100)
    plt.xlim(0,100)
    plt.show()



def algorithm(iteraciones,puntos,centroides,k):
    for i in range (iteraciones):
        puntos = asignarCentros(centroides, puntos,k)
        #PastC = centroides
        centroides = actu(centroides,puntos)
        imp(puntos,centroides)
        print("\n"*2)
        print("-----------------------------------")
        print("\n"*2)
        print("nuevos valores para los centroides: ")
        print(actu(centroides,puntos))
        #el siguiente fragmento de codigo no lo pude hacer andar, el objetivo era colocar un While para que se
        #repitiera hasta que no cambiara mas, pero por alguna razon PastC siempre era igual a centroides y cortaba a la
        #primera vuelta
        #if centroides.equals(PastC):
            #break
        #else:
            #print("funciona")

    print(puntos)
