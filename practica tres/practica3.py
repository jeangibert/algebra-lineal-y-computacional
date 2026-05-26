#Ejercicio 2b) chequeo de solucion!
import numpy as np

A=np.array([[1,-1,0,1],[0,1,4,0],[2,-1,0,-2],[-3,3,0,-1]])
L = np.array([[1,0,0,0],[0,1,0,0],[2,1,1,0],[-3,0,0,1]])
U = np.array([[1,-1,0,1],[0,1,4,0],[0,0,-4,-4],[0,0,0,2]])

print((A == L @ U).all())

#Ejercicio 3)
#a)


import numpy as np

"""
La idea de este ejercicio es la siguiente;
Debido a que es una matriz triangular lo que vamos a hacer es utilizar un i el cual vaya recorriendo las filas
y que tambien sirva como indicador para toparse con las paredes de 0 ya que como L es triangular inferior
la posicion de i concuerda con el ultimo elemento que no es 0 de la fila.
Luego lo que usaremos  es un j el cual nos servira de acumulador y que recorrera los y desde la primera columna
hasta la ultima y calcule el valor de ese y al despejarlo en la linea 21
Vamos a ir guardando los valores de Y en el array y que lo llenamos con 0.
Entonces iremos recorriendo cada fila con i , j calcularaa esa ecuacion de esa fila y lo guardaremos en el res
"""
def resolver_l_inferior(L:np.ndarray, b:np.ndarray):
    dimensiones = L.shape
    n = dimensiones[0]
    y = np.zeros(n)
    for i in range(n):
        suma_acumulada = 0
        for j in range(i):
            suma_acumulada += (L[i][j] * y[j])
        y[i]= (b[i] - suma_acumulada) / L[i][i]
    return y    
    
# PD : el b de este inciso se hace solo adaptando el codigo ( los indices de los fors ) pero el algoritmo
# es el mismo

