import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from src.auxiliares import *

MIN_JUEGOS = 0
MAX_JUEGOS = 500
SALTO = 50

def reconstruccion_vs_tiempo():
    """
    Muestra un gráfico con los tiempos de reconstruccion en función 
    de la cantidad de elementos en las listas que genera.
    """
    _tamanios = range(MIN_JUEGOS, MAX_JUEGOS, SALTO) 
    _tiempos = contar_tiempos_reconstruccion(_tamanios)
    tamanios = np.array(_tamanios)
    tiempos = np.array(_tiempos)

    params, cov = curve_fit(modelo_lineal, tamanios, tiempos)
    
    plt.scatter(tamanios, tiempos, label='Datos')
    tamanios_fit = np.linspace(min(tamanios), max(tamanios), 100)
    #tiempos_fit_cuad = modelo_cuadratico(tamanios_fit, *params)
    tiempos_fit_lin = modelo_lineal(tamanios_fit, *params)

    plt.title("Tiempo de Reconstrucción vs Cantidad de elementos")
    plt.plot(tamanios, tiempos, marker='o')
    plt.plot(tamanios_fit, tiempos_fit_lin, label='Ajuste lineal', color='red', linestyle='--')
    #plt.plot(tamanios_fit, tiempos_fit_lin, label='Ajuste lineal', color='green', linestyle='--')

    plt.xlabel("Cantidad de elementos en la lista")
    plt.ylabel("Tiempo de reconstruccion (ms)")
    plt.legend()
    plt.grid(True)
    plt.show()

