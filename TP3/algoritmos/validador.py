from auxiliares import es_contiguo, POSICIONES

def validador(restricciones_filas, restricciones_columnas, posiciones_barcos):
    """
    Dada una configuración de un tablero de batalla naval, verifica si cumple con las restricciones dadas.
    restricciones_filas: lista de enteros, donde restricciones_filas[i] es la cantidad de barcos que hay en la fila i.
    restricciones_columnas: lista de enteros, donde restricciones_columnas[j] es la cantidad de barcos que hay en la columna j.
    posiciones_barcos: set de conjuntos de tuplas, donde posiciones_barcos[i] es el conjunto de posiciones que ocupa el barco i.
    """
    n = len(restricciones_filas)
    m = len(restricciones_columnas)
    tablero_solucion = [[None] * m for _ in range(n)] 

    # contigüidad de barcos
    for set_barco in posiciones_barcos:
        for set_barco in posiciones_barcos:
            if len(set_barco) > 1:
                if not es_contiguo(set_barco):
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
            for dx, dy in [POSICIONES]:
                ni, nj = fila + dx, col + dy
                if 0 <= ni < n and 0 <= nj < m:
                    if tablero_solucion[ni][nj] is not None and tablero_solucion[ni][nj] != i:
                        return False

    return True
