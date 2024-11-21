import matplotlib.pyplot as plt
from algoritmos.leer_archivos import *
from algoritmos.aproximacion import *
import time
from algoritmos.auxiliares import  FACTOR_TIEMPO
from algoritmos.crear_juegos import generar_juego_random

LIMITE_MIN = 160
LIMITE_MAX = 1000
MIN_NUM_BARCOS = 50
CANT_JUEGOS_RANDOMS = 40

def aprox_tiempo_vs_matriz():
    archivos = leer_archivos(CARPETA)
    resultados = []
    for archivo in archivos:
        demandas_filas, demandas_columnas, barcos = leer_inputs('data/' + archivo)
        _, demanda_cumplida_esperada, demanda_total = leer_resultados_esperados('data/' + 'Resultados Esperados.txt', archivo)

        len_filas = len(demandas_filas)
        len_columnas = len(demandas_columnas)
        matriz = f'{len_filas}x{len_columnas}'
        cantidad_barcos = len(barcos)
        tablero = [[VACIO for _ in range(len_columnas)] for _ in range(len_filas)]

        # Medimos el tiempo de ejecución
        start_time = time.time()
        batalla_naval = aproximacion(tablero, demandas_filas, demandas_columnas, barcos)
        end_time = time.time()  
        tiempo_ejecucion = (end_time - start_time) * FACTOR_TIEMPO

        resultados.append((matriz, tiempo_ejecucion, len_filas * len_columnas, cantidad_barcos))

    for _ in range(CANT_JUEGOS_RANDOMS):
        restricciones_filas, restricciones_columnas, longitudes_barcos_colocados, _ = generar_juego_random(LIMITE_MIN, LIMITE_MAX, MIN_NUM_BARCOS)
        len_longitudes_barcos_colocados = len(longitudes_barcos_colocados)
        tablero = [[VACIO for _ in range(len(restricciones_columnas))] for _ in range(len(restricciones_filas))]
        start_time = time.time()
        batalla_naval = aproximacion(tablero, restricciones_filas, restricciones_columnas, longitudes_barcos_colocados)
        end_time = time.time()
        tiempo_ejecucion = (end_time - start_time) * FACTOR_TIEMPO
        resultados.append((f'{len(restricciones_filas)}x{len(restricciones_columnas)}', tiempo_ejecucion, len(restricciones_filas) * len(restricciones_columnas), len_longitudes_barcos_colocados))

    # Ordenar resultados por una proporcion de datos de entrada (n*m)^k
    resultados = sorted(resultados, key=lambda x: x[2]**x[3])

    # Extraer datos ordenados
    etiquetas = [f"{x[0]} ({x[3]} barcos)" for x in resultados]  # Etiquetas con matrices y cantidad de barcos
    tiempo_ejecucion = [x[1] for x in resultados]

    # Mostrar el resultado en plt
    plt.figure(figsize=(12, 7))
    plt.scatter(etiquetas, tiempo_ejecucion, label='Tiempo', color='blue')
    plt.plot(etiquetas, tiempo_ejecucion, linestyle='--', color='gray', alpha=0.6)
    plt.title("Tiempo de ejecución vs Proporcion de datos de entrada (n*m)^k")
    plt.xlabel("Tamaño de Matriz y Cantidad de Barcos")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.xticks(rotation=45, fontsize=10)  # Rotar las etiquetas para mejor visualización
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()