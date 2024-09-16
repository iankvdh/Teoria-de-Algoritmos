import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from src.auxiliares import *

def mostrar_cantidad_vs_tiempo(tamaños, tiempos):
    tamanios = np.array(tamaños)
    tiempos = np.array(tiempos)   

    params, cov = curve_fit(modelo_lineal, tamanios, tiempos)
    
    plt.scatter(tamanios, tiempos, label='Datos')
    tamanios_fit = np.linspace(min(tamanios), max(tamanios), 100)
    tiempos_fit = modelo_lineal(tamanios_fit, *params)

    plt.title("Tiempo de ejecución vs Cantidad de elementos")
    plt.plot(tamaños, tiempos, marker='o')
    plt.plot(tamanios_fit, tiempos_fit, label='Ajuste lineal', color='red', linestyle='--')

    plt.xlabel("Cantidad de elementos en la lista")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.legend()
    plt.grid(True)
    plt.show()
