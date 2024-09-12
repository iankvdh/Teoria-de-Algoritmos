import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from implementacion_optima import jugar
import random


N = 1000

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

def mostrar_cantidad_vs_puntos(tamaños, puntos_s, puntos_m):
    tamanios = np.array(tamaños)
    puntos_s = np.array(puntos_s)
    puntos_m = np.array(puntos_m)   

    plt.scatter(tamanios, puntos_s, label='Sophia')
    plt.scatter(tamanios, puntos_m, label='Mateo')
    plt.title("Puntos de Sophia y Mateo vs Cantidad de elementos")
    plt.plot(tamaños, puntos_s, marker='o')
    plt.plot(tamaños, puntos_m, marker='o')

    plt.xlabel("Cantidad de elementos en la lista")
    plt.ylabel("Cantidad de Puntos")
    plt.legend()
    plt.grid(True)
    plt.show()

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


def jugar_n_juegos(n):

    victorias_sofia = []

    for i in range(n):
        lista = random.sample(range(1, 999), 100)
        _, suma_sofia, suma_mateo = jugar(lista)
        
        diferencia = suma_sofia - suma_mateo
        if diferencia > 0:
            victorias_sofia.append(1)
        else:
            victorias_sofia.append(0)
    mostrar_veces_que_gano_sofia(victorias_sofia)



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