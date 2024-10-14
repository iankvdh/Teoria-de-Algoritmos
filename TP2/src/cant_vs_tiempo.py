import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from src.auxiliares import *

MIN_JUEGOS = 0
MAX_JUEGOS = 100
SALTO = 10

def mostrar_cantidad_vs_tiempo():
    """
    Muestra un gráfico con los tiempos de ejecución en función 
    de la cantidad de elementos en la lista.
    """
    _tamanios = range(MIN_JUEGOS, MAX_JUEGOS, SALTO) 
    _tiempos = contar_tiempos_juegos(_tamanios)
    tamanios = np.array(_tamanios)
    tiempos = np.array(_tiempos)

    params, cov = curve_fit(modelo_cuadratico, tamanios, tiempos)
    
    plt.scatter(tamanios, tiempos, label='Datos')
    tamanios_fit = np.linspace(min(tamanios), max(tamanios), 100)
    tiempos_fit = modelo_cuadratico(tamanios_fit, *params)

    plt.title("Tiempo de ejecución vs Cantidad de elementos")
    plt.plot(tamanios, tiempos, marker='o')
    plt.plot(tamanios_fit, tiempos_fit, label='Ajuste cuadrático', color='red', linestyle='--')

    plt.xlabel("Cantidad de elementos en la lista")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.legend()
    plt.grid(True)
    plt.show()
