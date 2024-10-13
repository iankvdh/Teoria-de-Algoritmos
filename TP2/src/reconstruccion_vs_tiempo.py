import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from src.auxiliares import *
from main import jugar
from main import reconstruir_monedas_tomadas_por_sophia

def reconstruccion_vs_tiempo(tamaños, listas):
    """
    Muestra un gráfico con los tiempos de reconstruccion en función 
    de la cantidad de elementos en la lista.
    """
    tiempos = reconstruir_muchos_arreglos(listas)
    tamanios = np.array(tamaños)
    tiempos = np.array(tiempos)   

    params, cov = curve_fit(modelo_cuadratico, tamanios, tiempos)
    
    plt.scatter(tamanios, tiempos, label='Datos')
    tamanios_fit = np.linspace(min(tamanios), max(tamanios), 100)
    tiempos_fit = modelo_cuadratico(tamanios_fit, *params)

    plt.title("Tiempo de Reconstrucción vs Cantidad de elementos")
    plt.plot(tamaños, tiempos, marker='o')
    plt.plot(tamanios_fit, tiempos_fit, label='Ajuste cuadrático', color='red', linestyle='--')

    plt.xlabel("Cantidad de elementos en la lista")
    plt.ylabel("Tiempo de reconstruccion (ms)")
    plt.legend()
    plt.grid(True)
    plt.show()

def reconstruir_muchos_arreglos(listas):
    """
    Dada una lista de listas de monedas, devuelve una lista con los tiempos de 
    reconstrucción de cada una de las listas. Además, devuelve dos listas con 
    los puntos de Sofia y Mateo respectivamente.
    """
    tiempos = []

    for i in listas:
        dp = jugar(i)
        inicio = time.perf_counter()
        reconstruir_monedas_tomadas_por_sophia(i, dp)
        fin = time.perf_counter()
        tiempos.append( (fin - inicio) * 1000) # milisegundos

    return tiempos
