#Ejercicio 2b) chequeo de solucion!
import numpy as np

A=np.array([[1,-1,0,1],[0,1,4,0],[2,-1,0,-2],[-3,3,0,-1]])
L = np.array([[1,0,0,0],[0,1,0,0],[2,1,1,0],[-3,0,0,1]])
U = np.array([[1,-1,0,1],[0,1,4,0],[0,0,-4,-4],[0,0,0,2]])

print((A == L @ U).all())