import matplotlib.pyplot as plt
from algoritmos.leer_archivos import *
from algoritmos.aproximacion import *

def aprox_cota():
    archivos = leer_todos_archivos(CARPETA)
    resultados = []
    for archivo in archivos:
        demandas_filas, demandas_columnas, barcos = leer_inputs('data/' + archivo)
        _, demanda_cumplida_esperada, demanda_total = leer_resultados_esperados('data/' + 'Resultados Esperados.txt', archivo)

        len_filas = len(demandas_filas)
        len_columnas = len(demandas_columnas)
        matriz = f'{len_filas}x{len_columnas}'
        cantidad_barcos = len(barcos)
        tablero = [[VACIO for _ in range(len_columnas)] for _ in range(len_filas)]

        batalla_naval = aproximacion(tablero, demandas_filas, demandas_columnas, barcos) # Resultado suboptimo
        
        n = len(tablero)
        m = len(tablero[0])
        cant = 0
        for i in range(n):
            for j in range(m):
                if tablero[i][j] != VACIO:
                    cant += 1
        demanda_subopt = cant*2 # Resultado suboptimo
        demanda_opt = demanda_cumplida_esperada # Resultado optimo

        resultados.append((matriz, len_filas * len_columnas, cantidad_barcos, demanda_subopt/demanda_opt ))

    # Ordenar resultados por una proporcion de datos de entrada (n*m)^k
    resultados = sorted(resultados, key=lambda x: x[3], reverse=True)

    # Extraer datos ordenados
    etiquetas = [f"{x[0]} ({x[2]} barcos)" for x in resultados]  # Etiquetas con matrices y cantidad de barcos
    factor_opt = [x[3] for x in resultados]
    
    # Encontrar mínimo de la cota
    min_valor = min(factor_opt)
    min_indice = factor_opt.index(min_valor)
    min_etiqueta = etiquetas[min_indice]

    # Mostrar el resultado en plt
    plt.figure(figsize=(12, 7))
    plt.plot(etiquetas, factor_opt, label='Cota decreciente (A(I) / z(A))', color='blue', marker='o')
    plt.fill_between(range(len(etiquetas)), factor_opt, alpha=0.2, color='blue')  # Área bajo la curva

    # Agregar texto para el valor mínimo
    plt.annotate(f"Mín: {min_valor:.2f}", 
                 (min_indice, min_valor), 
                 textcoords="offset points", 
                 xytext=(0, -15), 
                 ha='center', 
                 fontsize=10, 
                 color='red')
    
    # Líneas auxiliares para resaltar el mínimo
    plt.axhline(min_valor, linestyle="--", color="red", alpha=0.7)
    plt.axvline(min_indice, linestyle="--", color="red", alpha=0.7)

    plt.title("r'(A) vs Proporción de datos de entrada (n*m)^k")
    plt.xlabel("Tamaño de Matriz y Cantidad de Barcos")
    plt.ylabel("A(I) / z(A)")
    plt.xticks(rotation=45, fontsize=10)  # Rotar las etiquetas para mejor visualización
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()