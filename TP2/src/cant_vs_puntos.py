import matplotlib.pyplot as plt
import numpy as np
from src.auxiliares import *

MIN_JUEGOS = 100
MAX_JUEGOS = 2500
SALTO = 50


def mostrar_cantidad_vs_puntos():
    """
    Muestra un gráfico con los puntos de Sophia y Mateo en función 
    de la cantidad de elementos en la lista.
    """

    _tamanios = range(MIN_JUEGOS, MAX_JUEGOS, SALTO) 

    listas_de_monedas = []
    for tamanio in _tamanios:
        coins = generar_monedas(tamanio, 1)
        if coins.size == 0: # por alguna razon siempre el primer arreglo que genera es vacio
            coins = np.array([1])
        listas_de_monedas.append(coins)

    _, puntos_sofia, puntos_mateo = jugar_muchos_arreglos(listas_de_monedas)

    tamanios = np.array(_tamanios)
    puntos_s = np.array(puntos_sofia)
    puntos_m = np.array(puntos_mateo)   

    plt.scatter(tamanios, puntos_s, label='Sophia')
    plt.scatter(tamanios, puntos_m, label='Mateo')
    plt.title("Puntos de Sophia y Mateo vs Cantidad de elementos")
    plt.plot(tamanios, puntos_s, marker='o')
    plt.plot(tamanios, puntos_m, marker='o')

    plt.xlabel("Cantidad de elementos en la lista")
    plt.ylabel("Cantidad de Puntos")
    plt.legend()
    plt.grid(True)
    plt.show()