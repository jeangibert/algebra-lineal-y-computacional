import numpy as np
import matplotlib.pyplot as plt

def ejercicio18 (A:np.ndarray):
    #Primero genero los vectores aleatoriamente ,hay 2 maneras (las que vi xd):
    #Una seria usar la funcion que propone el ejercicio e ir con un for iterando 100 veces para ir agregandolo
    #a un array de arrays , me parece un quilombo
    #vectores_generados = np.random.random(1) -> esta seria la funcion que habria q iterar y añadir 100 veces
    #Segunda opcion y la que voy a usar es

    vectores_geneardores = np.random.uniform(-1,1,size=(A.shape[1],100))
    #Me ahorra el hecho de iterar y queda mas clean, el shape de a es para procurar que sea compatible el producto matriz
    #Hago la metodologia de torneo , voy comparando normas transformadas y me quedo con la de mayor valor!
    candidato : float = 0
    historial = []
    for vector in vectores_geneardores.T:
        vector_transformado = A @ vector
        if(np.any(vector)):
            norma_actual = np.linalg.norm(vector_transformado) / np.linalg.norm(vector)
            if (norma_actual>candidato):
                candidato = norma_actual
            historial.append(candidato)


    #Grafico genero los puntos

    n = np.arange(len(historial))
    plt.title("Estimacion de la norma 2 de la matriz ingresada")
    plt.xlabel("Numero de iteracion")
    plt.ylabel("Factor de estiramiento ||Ax|| / ||x||")

    plt.plot(n, historial, marker='o', markersize=4, color='red', label="Sucesión del Récord")
    plt.show()
    return candidato

matriz = np.array([[1, 2], [3, 4]])
print(ejercicio18(matriz))