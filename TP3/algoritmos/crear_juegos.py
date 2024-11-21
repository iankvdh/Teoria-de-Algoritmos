"""
CREACION DE UNA BATALLA NAVAL ALEATORIA
"""
import random

def generar_tablero(n, m): # O(n*m)
    """Genera un tablero vacío de tamaño n x m."""
    return [[None for _ in range(m)] for _ in range(n)]


def puede_colocar_barco(tablero, fila, columna, longitud, direccion): # O(n+m)
    """
    Verifica si es posible colocar un barco en la posición dada, respetando las restricciones de tablero,
    restricciones de adyacencia y restricciones de filas y columnas.
    """
    n, m = len(tablero), len(tablero[0])

    # Verificar si el barco cabe en el tablero
    if direccion == "H":
        if columna + longitud > m:
            return False
    elif direccion == "V":
        if fila + longitud > n:
            return False
    
    # Verificar los alrededores del barco
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(longitud): 
                if direccion == "H":
                    f, c = fila + i, columna + k + j
                elif direccion == "V":
                    f, c = fila + k + i, columna + j

                # Comprobar si la posición está dentro del tablero y si hay un barco
                if 0 <= f < n and 0 <= c < m:
                    if tablero[f][c] != None :
                        return False
    return True

def colocar_barco(tablero, fila, columna, longitud, direccion, barcos_colocados): # O(longitud)
    if direccion == "H":
        for c in range(columna, columna + longitud):
            tablero[fila][c] = barcos_colocados
    elif direccion == "V":
        for f in range(fila, fila + longitud):
            tablero[f][columna] = barcos_colocados

def generar_barcos(tablero, num_barcos): # O(n*m)
    """Coloca barcos en el tablero respetando las restricciones."""
    n, m = len(tablero), len(tablero[0])
    barcos_colocados = 0
    long_barcos_seleccionados = []

    while barcos_colocados < num_barcos:
        longitud = random.randint(1, 4)  # Barcos de longitud 1 a 4, se podría cambiar
        direccion = random.choice(["H", "V"])
        fila = random.randint(0, n - 1)
        columna = random.randint(0, m - 1)
            
        if puede_colocar_barco(tablero, fila, columna, longitud, direccion):
            colocar_barco(tablero, fila, columna, longitud, direccion, barcos_colocados)
            long_barcos_seleccionados.append(longitud)
            barcos_colocados += 1

    return list(long_barcos_seleccionados)

def generar_restricciones(tablero, num_barcos): # O(n+m)
    """Genera las restricciones de filas y columnas a partir de los barcos colocados."""
    n, m = len(tablero), len(tablero[0])
    restricciones_filas = [0] * n
    restricciones_columnas = [0] * m

    for i in range(n):
        for j in range(m):
            if tablero[i][j] != None:
                restricciones_filas[i] += 1
                restricciones_columnas[j] += 1

    return restricciones_filas, restricciones_columnas

def generar_juego_random(limite_min=5, limite_max=10, min_num_barcos=2):
    n = random.randint(limite_min, limite_max) 
    m = random.randint(limite_min, limite_max) 
    num_barcos = random.randint(min_num_barcos, min(n, m))

    tablero = generar_tablero(n, m) # O(n*m)

    longitudes_barcos_colocados = generar_barcos(tablero, num_barcos) # O(n*m)
    restricciones_filas, restricciones_columnas = generar_restricciones(tablero, num_barcos) # O(n+m)
    acumulacion_esperada = 0
    for i in range(n):
        acumulacion_esperada += restricciones_filas[i]
    for j in range(m):
        acumulacion_esperada += restricciones_columnas[j]
    
    return restricciones_filas, restricciones_columnas, longitudes_barcos_colocados, acumulacion_esperada

# O(n*m)
