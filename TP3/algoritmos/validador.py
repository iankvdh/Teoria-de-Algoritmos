from algoritmos.auxiliares import es_contiguo, configurar_posiciones_barcos, POSICIONES
from algoritmos.leer_archivos import leer_inputs, leer_resultados_esperados, leer_resultados_validador

def validador(restricciones_filas, restricciones_columnas, posiciones_barcos, barcos, demanda_cumplida, demanda_total):
    """
    Dada una configuración de un tablero de batalla naval, verifica si cumple con las restricciones dadas.
    restricciones_filas: lista de enteros, donde restricciones_filas[i] es la cantidad de barcos que hay en la fila i.
    restricciones_columnas: lista de enteros, donde restricciones_columnas[j] es la cantidad de barcos que hay en la columna j.
    posiciones_barcos: set de conjuntos de tuplas, donde posiciones_barcos[i] es el conjunto de posiciones que ocupa el barco i.
    """
    # demanda cumplida
    if sum(restricciones_filas) + sum(restricciones_columnas) != demanda_cumplida:
        return False
    
    # demanda total
    if demanda_cumplida != demanda_total:
        return False

    n = len(restricciones_filas)
    m = len(restricciones_columnas)
    tablero_solucion = [[None] * m for _ in range(n)] 

    # cantidad de barcos
    if len(posiciones_barcos) != len(barcos):
        return False
    
    # contigüidad de barcos
    for set_barco in posiciones_barcos:
        if set_barco is None:
            continue
        if len(set_barco) > 1:
            if not es_contiguo(set_barco):           
                return False

    # cantidad de posiciones que ocupa cada barco
    for i, set_barco in enumerate(posiciones_barcos):
        if set_barco is not None:
            if len(set_barco) != barcos[i]:
                return False

    for i, set_barco in enumerate(posiciones_barcos):
        if set_barco is not None:
            for (fila, col) in set_barco:
                tablero_solucion[fila][col] = i

    # restricciones filas
    for i in range(n):
        ocupados_en_fila = sum(1 for j in range(m) if tablero_solucion[i][j] is not None)
        if ocupados_en_fila != restricciones_filas[i]:
            return False

    # restricciones columnas
    for j in range(m):
        ocupados_en_col = sum(1 for i in range(n) if tablero_solucion[i][j] is not None)
        if ocupados_en_col != restricciones_columnas[j]:
            return False

    # restricciones adyacencias
    for i, set_barco in enumerate(posiciones_barcos):
        for (fila, col) in set_barco:
            for dx, dy in POSICIONES:
                ni, nj = fila + dx, col + dy
                if 0 <= ni < n and 0 <= nj < m:
                    if tablero_solucion[ni][nj] is not None and tablero_solucion[ni][nj] != i:
                        return False

    return True

def mostrar_resultados_ruta_abs_validador(ruta_absoluta_archivo, ruta_absoluta_resultados):
    demandas_filas, demandas_columnas, barcos = leer_inputs(ruta_absoluta_archivo)
    posiciones_barcos, demanda_cumplida, demanda_total = leer_resultados_esperados(ruta_absoluta_resultados)
    pos_barcos = configurar_posiciones_barcos(posiciones_barcos)
    if validador(demandas_filas, demandas_columnas, pos_barcos, barcos, demanda_cumplida, demanda_total):
        print(f"El archivo {ruta_absoluta_archivo} es válido.")
    else:
        print(f"El archivo {ruta_absoluta_archivo} es inválido.")
