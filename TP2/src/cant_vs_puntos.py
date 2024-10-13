import matplotlib.pyplot as plt
import numpy as np
from src.auxiliares import *

def mostrar_cantidad_vs_puntos(tamaños, puntos_s, puntos_m):
    """
    Muestra un gráfico con los puntos de Sophia y Mateo en función 
    de la cantidad de elementos en la lista.
    """
    tamanios = np.array(tamaños)
    puntos_s = np.array(puntos_s)
    puntos_m = np.array(puntos_m)   

    plt.scatter(tamanios, puntos_s, label='Sophia')
    plt.scatter(tamanios, puntos_m, label='Mateo')
    plt.title("Puntos de Sophia y Mateo vs Cantidad de elementos")
    plt.plot(tamaños, puntos_s, marker='o')
    plt.plot(tamaños, puntos_m, marker='o')

    plt.xlabel("Cantidad de elementos en la lista")
    plt.ylabel("Cantidad de Puntos")
    plt.legend()
    plt.grid(True)
    plt.show()