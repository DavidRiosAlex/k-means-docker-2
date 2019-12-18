***En este repositorio estare subiendo las actualizaciones que le haga al script, por el momento el script posee tres versiones:***


**kmeans0.1**:
  Esta version tiene muchos valores por default, con una unica interaccion (modificar la cantidad de iteraciones) 
  
  
**kmeans0.2**:
  Esta version se le agrego opciones para interactuar modificando las interacciones y la cantidad de puntos de 
  ejemplos que existen. (se cambiaron ademas algunas funciones pero continua funcionando de la misma manera que la version 0.1
  a diferencia de algunos decimales en las distancias y o ubicacion de los centroides) 
  
**kmeans1.0**:
  Se agrego una nueva opcion que deja al usuario elegir entre que base de datos usar( circulos o flores iris ), se implemento 
  el realizar un random de los centroides, atraves de los puntos ya existentes en los datasets, de esta manera se intentaba 
  tratar de corregir el problema de que el programa se cortara, lanzando un error de division por 0 demasiado seguido, cuando                            
  un centroide no tenia puntos para actuar como centro, se agrego una impresion por pantalla de un dataset al final del
  algoritmo que proporciona la informacion de el promedio de las distancias de los puntos con su correspondiente centroide
  cercano, con respecto a la cantidad de centroides que se agregaban, de esta manera tambien podemos observar por cuantos
  centroides optar en este algoritmo.

**kmeans2.0**:
  Una version mejorada de 1.0 que es capaz de procesar datos de n dimensiones y no solo de dos dimensiones como lo era la 1.0.
  A su vez agregamos 1 interaccion mas, "k", que define la cantidad maxima de centroides a procesar.
