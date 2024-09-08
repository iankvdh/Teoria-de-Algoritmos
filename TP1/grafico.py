import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from implementacion_optima import jugar

def leer_numeros_desde_txt(nombre_archivo):
    nombre_archivo = 'data/' + nombre_archivo

    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read().strip()  
        numeros_str = contenido.split(';')  
        numeros = [int(num) for num in numeros_str]  
    return numeros

def modelo_lineal(x, m, b):
    return m * x + b

def modelo_cuadratico(x, a, b, c):
    return a * x**2 + b * x + c

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

def main():
    listas = []
    tamaños = []

    for i in ["20.txt","25.txt","50.txt","100.txt","1000.txt","5000.txt","10000.txt","15000.txt","20000.txt", "25000.txt", "30000.txt"]:
        lista = leer_numeros_desde_txt(i)
        listas.append(lista)
        tamaños.append(len(lista))

    tiempos = []

    for i in listas:
        inicio = time.perf_counter()
        jugar(i)
        fin = time.perf_counter()
        tiempos.append( (fin - inicio) * 1000) # Convertir el tiempo a milisegundos

    mostrar_cantidad_vs_tiempo(tamaños, tiempos)

main()