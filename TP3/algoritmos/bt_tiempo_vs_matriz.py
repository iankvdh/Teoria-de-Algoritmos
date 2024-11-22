import matplotlib.pyplot as plt
from algoritmos.leer_archivos import *
from algoritmos.backtracking import *
import time
from algoritmos.auxiliares import  FACTOR_TIEMPO

def bt_mostrar_tiempo_vs_matriz():
    archivos = leer_archivos(CARPETA)
    resultados = []
    for archivo in archivos:
        demandas_filas, demandas_columnas, barcos = leer_inputs('data/' + archivo)
        _, demanda_cumplida_esperada, demanda_total = leer_resultados_esperados('data/' + 'Resultados Esperados.txt', archivo)

        len_filas = len(demandas_filas)
        len_columnas = len(demandas_columnas)
        matriz = f'{len_filas}x{len_columnas}'
        cantidad_barcos = len(barcos)

        # Medimos el tiempo de ejecución
        start_time = time.time()
        batalla_naval = Batalla_Naval(demandas_filas, demandas_columnas, barcos)
        end_time = time.time()  
        tiempo_ejecucion = (end_time - start_time) * FACTOR_TIEMPO

        resultados.append((matriz, tiempo_ejecucion, len_filas * len_columnas, cantidad_barcos))


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
