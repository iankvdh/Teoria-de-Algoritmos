import numpy as np
import time
import matplotlib.pyplot as plt
from main import jugar

from src.auxiliares import generar_monedas

def ejecutar_simulaciones_variabilidad(tamaños, niveles_variabilidad, tiempos_ejecucion):
    """
    Ejecuta la simulación para cada tamaño y cada nivel de variabilidad
    """
    for variabilidad in niveles_variabilidad:
        for tamaño in tamaños:
            # Generar el arreglo de monedas con el nivel de variabilidad dado
            coins = generar_monedas(tamaño, variabilidad)
            
            # Medir el tiempo de ejecución de la función 'jugar'
            start_time = time.time()
            jugar(coins)  # Ejecutamos la función
            end_time = time.time()
            
            # Guardamos el tiempo de ejecución
            tiempo = end_time - start_time
            tiempos_ejecucion[variabilidad].append(tiempo)

def mostrar_tiempo_vs_variabilidad():
    # Lista de tamaños de ejemplos que vamos a probar
    tamaños = range(10, 1101, 10)  # de 10 a 300 monedas, en pasos de 10

    # Lista de niveles de variabilidad que queremos probar
    niveles_variabilidad = [0.5, 1, 1.5, 2, 3, 4] 
    colores = ['b', 'orange', 'g', 'r', 'yellow', 'purple']  # Colores para el gráfico

    # Diccionario para almacenar los tiempos de ejecución
    tiempos_ejecucion = {variabilidad: [] for variabilidad in niveles_variabilidad}

    ejecutar_simulaciones_variabilidad(tamaños, niveles_variabilidad, tiempos_ejecucion)

    plt.figure(figsize=(10, 6))

    for i, variabilidad in enumerate(niveles_variabilidad):
        plt.plot(tamaños, tiempos_ejecucion[variabilidad], marker='o', color=colores[i], label=f'Variabilidad {variabilidad}')

    plt.title('Tiempo de ejecución en función de la variabilidad de datos')
    plt.xlabel('Tamaño del ejemplo')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.legend()
    plt.grid(True)
    plt.show()