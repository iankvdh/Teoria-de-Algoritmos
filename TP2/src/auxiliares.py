import os
import numpy as np
from main import jugar
from main import reconstruir_monedas_tomadas_por_sophia
import time

FACTOR_TIEMPO = 1000 # milisegundos


def modelo_lineal(x, m, b):
    return m * x + b

def modelo_cuadratico(x, a, b, c):
    return a * x**2 + b * x + c


def generar_monedas(tamaño, variabilidad):
    """
    Genera un arreglo de monedas con un tamaño dado y un nivel de variabilidad
    """
    return np.random.randint(1, int(100 * variabilidad), tamaño)


def contar_tiempos_reconstruccion(tamanios):
    """ 
    Dada una lista de listas de monedas, devuelve una lista con los tiempos de 
    reconstrucción de cada una de las listas. Además, devuelve dos listas con 
    los puntos de Sofia y Mateo respectivamente.
    """
    tiempos = []
    
    for tamanio in tamanios:
        coins = generar_monedas(tamanio, 1)
        dp = jugar(coins)
        inicio = time.perf_counter()
        reconstruir_monedas_tomadas_por_sophia(coins, dp)
        fin = time.perf_counter()
        tiempos.append( (fin - inicio) * FACTOR_TIEMPO) # milisegundos

    return tiempos


def contar_tiempos_juegos(tamanios):
    """ 
    Dada una lista de listas de monedas, devuelve una lista con los tiempos de 
    reconstrucción de cada una de las listas. Además, devuelve dos listas con 
    los puntos de Sofia y Mateo respectivamente.
    """
    tiempos = []
    
    for tamanio in tamanios:
        coins = generar_monedas(tamanio, 1)
        inicio = time.perf_counter()
        jugar(coins)
        fin = time.perf_counter()
        tiempos.append( (fin - inicio) * FACTOR_TIEMPO) # milisegundos

    return tiempos


def jugar_muchos_arreglos(listas):
    """
    Dada una lista de listas de monedas, devuelve una lista con los tiempos de ejec
    de cada una de las listas. Además, devuelve dos listas con los puntos de Sofia
    y Mateo respectivamente.
    """
    tiempos = []
    puntos_sofia = []
    puntos_mateo = []

    for i in listas:
        inicio = time.perf_counter()
        dp = jugar(i)
        suma_sofia = dp[0][-1]
        suma_mateo = sum(i) - suma_sofia
        puntos_sofia.append(suma_sofia)
        puntos_mateo.append(suma_mateo)
        fin = time.perf_counter()
        tiempos.append( (fin - inicio) * FACTOR_TIEMPO) # milisegundos

    return tiempos, puntos_sofia, puntos_mateo
