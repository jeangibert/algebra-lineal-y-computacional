#Ejercicio 2b) chequeo de solucion!
import numpy as np

A=np.array([[1,-1,0,1],[0,1,4,0],[2,-1,0,-2],[-3,3,0,-1]])
L = np.array([[1,0,0,0],[0,1,0,0],[2,1,1,0],[-3,0,0,1]])
U = np.array([[1,-1,0,1],[0,1,4,0],[0,0,-4,-4],[0,0,0,2]])

print((A == L @ U).all())

#Ejercicio 3)
#a)

def solucionadorTriangularesInferiores(matriz,resultado):
    """
    Idea (a11,0,0      (y1)       (b1)
          a21,a22,0    (y2)     = (b2)
          a31,a32,a33) (y3)       (b3)

    y1 = b1/a11
    
    
    """