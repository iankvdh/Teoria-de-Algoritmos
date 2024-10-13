import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from src.auxiliares import *

def reconstruccion_vs_tiempo(tamaños, tiempos):
    """
    Muestra un gráfico con los tiempos de reconstruccion en función 
    de la cantidad de elementos en la lista.
    """
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
