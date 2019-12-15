import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from IPython.display import clear_output
#np.random.seed(200) fija los puntos random con el seed 200 puede ser eliminado para ejecutar puntos
#siempre distintos
np.random.seed(100)

#esta operacion asigna los centroides a una zona del eje de coordenadas
def asignarCentros(centroides,puntos,k,colores=['red','blue','green']):
    for i in centroides.keys():


        #se asigna los valores de las operaciones para x y para y
        x = ((puntos['x'] - centroides[i][0]) ** 2)
        y = (puntos['y'] - centroides[i][1]) ** 2


        #se saca la raiz cuadrada de la suma de los dos anteriores
        res = np.sqrt(x+y)


        #se crea (y si ya esta creada se asigna) la llave "distancia a p" con la vuelta i y a la misma se le da el
        #valor res 
        puntos['p'+str(i)] = res

    # se crea la llave 'cercano a', y almacena en ella el centroide mas cercano al punto
    puntos['cercano a'] = puntos.loc[:,[('p'+str(i)) for i in centroides]].idxmin(axis=1)


    #se le asigna un color a cada punto correspondiente al conjunto de datos que pertenece a un centroide n
    #en el dataframe
    puntos['color'] = puntos['cercano a'].map(lambda x: colores[int(x.lstrip('p'))])


    #y se regresa el dataframe modificado 
    return puntos

         
def actu(puntos,centroides):
    #el centroide cambia de posicion segun el promedio de todos los puntos en x e y, que corresponden 
    # al centroide operando
    for i in centroides.keys():
        a = np.mean(puntos[puntos['cercano a'] == ('p'+str(i))]['x'])
        b = np.mean(puntos[puntos['cercano a'] == ('p'+str(i))]['y'])
        centroides[i][0],centroides[i][1] = a,b
    return centroides


def imp(puntos,centroides,colores):

    #graficacion
    ventana = plt.figure(1,figsize = (6,6))
    plt.scatter(puntos['x'], puntos['y'], color=puntos['color'], alpha=0.8, edgecolor='k')
    for i in centroides.keys():
        plt.scatter(*centroides[i], color='black')
    plt.show()



def algorithm(puntos,centroides,k,colores):
    #for i in range (iteraciones):
    puntos = asignarCentros(centroides, puntos,k,colores)
        #PastC = centroides
    centroides = actu(puntos,centroides)
    imp(puntos,centroides,colores)
    print("\n"*2)
    print("-----------------------------------")
    print("\n"*2)
    print("nuevos valores para los centroides: ")
    print(centroides)
    clear_output(wait=True)
        #time.sleep(5)
        #el siguiente fragmento de codigo no lo pude hacer andar, el objetivo era colocar un While para que se
        #repitiera hasta que no cambiara mas, pero por alguna razon PastC siempre era igual a centroides y cortaba a la
        #primera vuelta
        #if centroides.equals(PastC):
            #break
        #else:
            #print("funciona")
    return puntos,centroides

def cost(puntos,centroides):
    for i in centroides.keys():
        min = np.mean(puntos[puntos['cercano a']==('p'+str(i))][('p'+str(i))])
    cost = np.mean(min)
    return cost