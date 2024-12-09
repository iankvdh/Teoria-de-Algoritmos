# Dado un tablero de ajedrez n×n, implementar un algoritmo por backtracking que ubique (si es posible) 
# a n reinas de tal manera que ninguna pueda comerse con ninguna.

VACIO = 0
REINA = 1

def es_compatible(tablero, fila, columna):
    # chequeo si hay una reina en la misma fila
    for i in range(len(tablero)):
        if tablero[fila][i] == REINA:
            return False
    # chequeo si hay una reina en la misma columna
    for i in range(len(tablero)):
        if tablero[i][columna] == REINA:
            return False
    # chequeo si hay una reina en la diagonal principal
    for i in range(len(tablero)):
        if fila + i < len(tablero) and columna + i < len(tablero):
            if tablero[fila + i][columna + i] == REINA:
                return False
        if fila - i >= 0 and columna - i >= 0:
            if tablero[fila - i][columna - i] == REINA:
                return False
    # chequeo si hay una reina en la diagonal secundaria
    for i in range(len(tablero)):
        if fila + i < len(tablero) and columna - i >= 0:
            if tablero[fila + i][columna - i] == REINA:
                return False
        if fila - i >= 0 and columna + i < len(tablero):
            if tablero[fila - i][columna + i] == REINA:
                return False
    return True

def n_reinas(n):
    tablero = [[VACIO for i in range(n)] for j in range(n)]
    if n == 0:
        return []
    cantidad_reinas = 0
    n_reinas_aux(tablero, n, 0, 0, cantidad_reinas)
    res = []
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == REINA:
                res.append((i, j))
    return res

def n_reinas_aux(tablero, n, fila, columna, cantidad_reinas):
    if cantidad_reinas == n:
        return True
    if fila == len(tablero):
        return False
    if columna == len(tablero):
        return n_reinas_aux(tablero, n, fila + 1, 0, cantidad_reinas)
    
    if es_compatible(tablero, fila, columna):
        tablero[fila][columna] = REINA
        if n_reinas_aux(tablero, n, fila, columna + 1, cantidad_reinas + 1):
            return True
    tablero[fila][columna] = VACIO
    return n_reinas_aux(tablero, n, fila, columna + 1, cantidad_reinas)

def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)

tablero = [[VACIO for i in range(3)] for j in range(3)]
n_reinas(tablero, 2)
imprimir_tablero(tablero)