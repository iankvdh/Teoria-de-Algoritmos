import matplotlib.pyplot as plt
import numpy as np
from main import jugar
import random
from src.auxiliares import *

N = 1000 # Cantidad de juegos default
# MIN_RANDOM_RANGE < MAX_RANDOM_RANGE
MIN_RANDOM_RANGE = 1
MAX_RANDOM_RANGE = 999
MAX_CANT_MONEDAS = 1000 # Cantidad máxima de monedas
VIC_SOPHIA = 1
VIC_MATEO = 0

def mostrar_veces_que_gano_sofia(victorias_sofia):
    """
    Muestra un gráfico con las veces que ganó Sophia en función de la cantidad de juegos.
    """
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
    """
    Juega n juegos y muestra un gráfico con las veces que ganó Sophia.
    """
    victorias_sofia = []
    listas = []
    for _ in range(n):
        cantidad_monedas = random.randint(1, MAX_CANT_MONEDAS)
        lista = [random.randint(MIN_RANDOM_RANGE, MAX_RANDOM_RANGE) for _ in range(cantidad_monedas)]
        listas.append(lista)

    for lista in listas:
        dp = jugar(lista)
        suma_sofia = dp[0][-1]
        suma_mateo = sum(lista) - suma_sofia
        diferencia = suma_sofia - suma_mateo
        if diferencia > 0:
            victorias_sofia.append(VIC_SOPHIA)
        else:
            victorias_sofia.append(VIC_MATEO)
    mostrar_veces_que_gano_sofia(victorias_sofia)