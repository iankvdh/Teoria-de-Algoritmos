import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from implementacion_optima import jugar
import random
from src.auxiliares import *


def mostrar_veces_que_gano_sofia(victorias_sofia):
    tamanios = np.arange(1, len(victorias_sofia)+1)
    victorias_sofia = np.array(victorias_sofia)
    plt.scatter(tamanios, victorias_sofia, label='Victoria')
    plt.title("Veces que ganó Sophia vs Cantidad de juegos")
    plt.plot(tamanios, victorias_sofia, marker='o')

    plt.xlabel("Cantidad de juegos")
    plt.ylabel("1 si ganó Sophia, 0 si no")
    plt.legend()
    plt.grid(True)
    plt.show()

def jugar_n_juegos(n):

    victorias_sofia = []

    for i in range(n):
        lista = random.sample(range(1, 999), 100)
        _, suma_sofia, suma_mateo = jugar(lista)
        
        diferencia = suma_sofia - suma_mateo
        if diferencia > 0:
            victorias_sofia.append(1)
        else:
            victorias_sofia.append(0)
    mostrar_veces_que_gano_sofia(victorias_sofia)