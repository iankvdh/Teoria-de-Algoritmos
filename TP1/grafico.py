import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from implementacion_optima import jugar
import random
from src.auxiliares import *
from src.jugar_n_juegos import jugar_n_juegos
from src.cant_vs_tiempo import mostrar_cantidad_vs_tiempo
from src.cant_vs_puntos import mostrar_cantidad_vs_puntos

N = 1000

def main():
    listas = []
    tamaños = []
    puntos_sofia = []
    puntos_mateo = []

    for i in ["20.txt","25.txt","50.txt","100.txt","1000.txt","5000.txt","10000.txt","15000.txt","20000.txt", "25000.txt", "30000.txt"]:
        lista = leer_numeros_desde_txt(i)
        listas.append(lista)
        tamaños.append(len(lista))

    tiempos = []

    for i in listas:
        inicio = time.perf_counter()
        _, suma_sofia, suma_mateo = jugar(i)
        puntos_sofia.append(suma_sofia)
        puntos_mateo.append(suma_mateo)
        fin = time.perf_counter()
        tiempos.append( (fin - inicio) * 1000) # Convertir el tiempo a milisegundos

    jugar_n_juegos(N)
    mostrar_cantidad_vs_tiempo(tamaños, tiempos)
    mostrar_cantidad_vs_puntos(tamaños, puntos_sofia, puntos_mateo)

main()