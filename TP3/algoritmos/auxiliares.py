# Funciones auxiliares para el TP3

# CONSTANTES
HORIZONTAL = 0
VERTICAL = 1
BARCO = 1

# POSICIONES
IZQ_ARRIBA = (-1, -1)
DER_ARRIBA = (-1, 1)
ARRIBA = (-1, 0)
ABAJO = (1, 0)
IZQ = (0, -1)
DER = (0, 1)
IZQ_ABAJO = (1, -1)
DER_ABAJO = (1, 1)
POSICIONES = [IZQ_ARRIBA, DER_ARRIBA, ARRIBA, ABAJO, IZQ, DER, IZQ_ABAJO, DER_ABAJO]

def es_contiguo(set_barco):
    posiciones = list(set_barco)
    visitados = set()
    pila = [posiciones[0]]
    
    while pila:
        (fila, col) = pila.pop()
        if (fila, col) not in visitados:
            visitados.add((fila, col))
            
            # Revisamos las posiciones adyacentes
            for dx, dy in [ARRIBA, IZQ, DER, ABAJO]:
                adyacente = (fila + dx, col + dy)
                if adyacente in set_barco and adyacente not in visitados:
                    pila.append(adyacente)
    
    return len(visitados) == len(set_barco)

def calcular_demanda_incumplida(tablero, restricciones_filas, restricciones_columnas):
    """
    Dado un tablero de dimensiones n x m, una lista de restricciones para las filas y columnas, y una lista de barcos con sus posiciones y orientaciones,
    la demanda incumplida es la cantidad de barcos que faltan para cumplir con las restricciones de filas y columnas.
    """
    n = len(tablero)
    m = len(tablero[0])
    demanda_incumplida = 0
    # Calcular incumplimiento en filas
    for i in range(n):
        ocupados = sum(tablero[i])
        demanda_incumplida += max(0, restricciones_filas[i] - ocupados)
    # Calcular incumplimiento en columnas
    for j in range(m):
        ocupados = sum(tablero[i][j] for i in range(n))
        demanda_incumplida += max(0, restricciones_columnas[j] - ocupados)
    return demanda_incumplida

def es_posicion_valida(fila, columna, n, m):
    return 0 <= fila < n and 0 <= columna < m

def verificar_adyacencias(tablero, fila, columna, orientacion, longitud):
    n = len(tablero)
    m = len(tablero[0])
        
    if orientacion == HORIZONTAL:
        # Verificar los extremos izquierdo y derecho del barco
        if columna > 0:  # Verificar celda a la izquierda del barco
            for dx, dy in [IZQ_ARRIBA, IZQ, IZQ_ABAJO]:
                ni, nj = fila + dx, columna + dy
                if es_posicion_valida(ni, nj, n, m) and tablero[ni][nj] == BARCO:
                    return False
        if columna + longitud < m:  # Verificar celda a la derecha del barco
            for dx, dy in [DER_ARRIBA, DER, DER_ABAJO]:
                ni, nj = fila + dx, columna + longitud + dy
                if es_posicion_valida(ni, nj, n, m) and tablero[ni][nj] == BARCO:
                    return False

        # Verificar celdas arriba y abajo de cada parte del barco
        for j in range(columna, columna + longitud):
            if fila > 0:  # Verificar celdas arriba del barco
                if tablero[fila - 1][j] == BARCO:
                    return False
            if fila + 1 < n:  # Verificar celdas abajo del barco
                if tablero[fila + 1][j] == BARCO:
                    return False

    elif orientacion == VERTICAL:
        # Verificar los extremos superior e inferior del barco
        if fila > 0:  # Verificar celda encima del barco
            for dx, dy in [IZQ_ARRIBA, ARRIBA, DER_ARRIBA]:
                ni, nj = fila + dx, columna + dy
                if es_posicion_valida(ni, nj, n, m) and tablero[ni][nj] == BARCO:
                    return False
        if fila + longitud < n:  # Verificar celda debajo del barco
            for dx, dy in [IZQ_ABAJO, ABAJO, DER_ABAJO]:
                ni, nj = fila + longitud + dx, columna + dy
                if es_posicion_valida(ni, nj, n, m) and tablero[ni][nj] == BARCO:
                    return False

        # Verificar celdas izquierda y derecha de cada parte del barco
        for i in range(fila, fila + longitud):
            if columna > 0:  # Verificar celdas a la izquierda del barco
                if tablero[i][columna - 1] == BARCO:
                    return False
            if columna + 1 < m:  # Verificar celdas a la derecha del barco
                if tablero[i][columna + 1] == BARCO:
                    return False

    return True


def verificar_restriccion_fila(tablero, fila, inicio, longitud, restriccion_fila):
    ocupados_en_fila = sum(tablero[fila][inicio : inicio + longitud])
    return ocupados_en_fila <= restriccion_fila


def verificar_restriccion_columna(tablero, columna, inicio, longitud, restriccion_columna):
    ocupados_en_columna = sum(tablero[i][columna] for i in range(inicio, inicio + longitud))
    return ocupados_en_columna <= restriccion_columna


def es_compatible(tablero, restricciones_filas, restricciones_columnas, i, j, barco, orientacion):
    # ver que no haya barcos adyacentes
    # y se cumplan las reestricciones por fila y columna
    longitud = barco
    fila = i
    columna = j
    if orientacion == HORIZONTAL:
        # Verificar restricciones de fila para el barco horizontal
        if not verificar_restriccion_fila(tablero, fila, columna, longitud, restricciones_filas[fila]):
            return False
        
        # Verificar restricciones de columna para cada posición ocupada por el barco
        for j in range(columna, columna + longitud):
            if not verificar_restriccion_columna(tablero, j, fila, 1, restricciones_columnas[j]):
                return False
    else:
        # Verificar restricciones de columna para el barco vertical
        if not verificar_restriccion_columna(tablero, columna, fila, longitud, restricciones_columnas[columna]):
            return False
        
        # Verificar restricciones de fila para cada posición ocupada por el barco
        for i in range(fila, fila + longitud):
            if not verificar_restriccion_fila(tablero, i, columna, 1, restricciones_filas[i]):
                return False

    # Verificar adyacencias
    return verificar_adyacencias(tablero, fila, columna, orientacion, longitud)
