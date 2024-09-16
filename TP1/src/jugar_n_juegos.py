import matplotlib.pyplot as plt
import numpy as np
from implementacion_optima import jugar
import random
from src.auxiliares import *

N = 1000
RANDOM_RANGE = range(1, 999)
VIC_SOPHIA = 1
VIC_MATEO = 0

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

def jugar_n_juegos(n = N):

    victorias_sofia = []

    for i in range(n):
        lista = random.sample(RANDOM_RANGE, 100)
        _, suma_sofia, suma_mateo = jugar(lista)
        
        diferencia = suma_sofia - suma_mateo
        if diferencia > 0:
            victorias_sofia.append(VIC_SOPHIA)
        else:
            victorias_sofia.append(VIC_MATEO)
    mostrar_veces_que_gano_sofia(victorias_sofia)