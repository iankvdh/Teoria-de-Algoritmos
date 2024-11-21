"""
CREACION DE UNA BATALLA NAVAL ALEATORIA
"""
import random

def generar_tablero(n, m): # O(n*m)
    """Genera un tablero vacío de tamaño n x m."""
    return [[None for _ in range(m)] for _ in range(n)]

def restricciones_aleatorias(n, m, max_barcos): # O(n+m)
    """Genera restricciones aleatorias para filas y columnas."""
    restricciones_filas = [random.randint(0, max_barcos) for _ in range(n)]
    restricciones_columnas = [random.randint(0, max_barcos) for _ in range(m)]
    return restricciones_filas, restricciones_columnas

def puede_colocar_barco(tablero, fila, columna, longitud, direccion, restricciones_filas, restricciones_columnas): # O(n+m)
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
        
    # Verificar restricciones de filas y columnas
    if direccion == "H":
        # si al sumar la long del barco y los barcos que esten puestos en la fila es mayor a la restriccion de la fila
        if sum(1 for c in range(m) if tablero[fila][c] != None) + longitud > restricciones_filas[fila]: # O(m)
            return False
        for c in range(columna, columna + longitud): # O(longitud)
            if restricciones_columnas[c] == 0:
                return False
    elif direccion == "V":
        # si al sumar la long del barco y los barcos que esten puestos en la columna es mayor a la restriccion de la columna
        if sum(1 for f in range(n) if tablero[f][columna] != None) + longitud > restricciones_columnas[columna]: # O(n)
            return False
        for f in range(fila, fila + longitud): # O(longitud)
            if restricciones_filas[f] == 0:
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

def generar_barcos(tablero, restricciones_filas, restricciones_columnas, num_barcos): # O(n*m)
    """Coloca barcos en el tablero respetando las restricciones."""
    n, m = len(tablero), len(tablero[0])
    barcos_colocados = 0
    long_barcos_seleccionados = []

    while barcos_colocados < num_barcos:
        longitud = random.randint(1, 4)  # Barcos de longitud 1 a 4, se podría cambiar
        direccion = random.choice(["H", "V"])
        fila = random.randint(0, n - 1)
        columna = random.randint(0, m - 1)
            
        if puede_colocar_barco(tablero, fila, columna, longitud, direccion, restricciones_filas, restricciones_columnas):
            colocar_barco(tablero, fila, columna, longitud, direccion, barcos_colocados)
            long_barcos_seleccionados.append(longitud)
            barcos_colocados += 1

            # Actualizar restricciones
            if direccion == "H":
                restricciones_filas[fila] -= longitud
                for c in range(columna, columna + longitud):
                    restricciones_columnas[c] -= 1
            elif direccion == "V":
                restricciones_columnas[columna] -= longitud
                for f in range(fila, fila + longitud):
                    restricciones_filas[f] -= 1

    return list(long_barcos_seleccionados)

def generar_juego_random(min_filas=5, min_columnas=10, num_barcos=2):
    n = random.randint(min_filas, min_columnas) 
    m = random.randint(min_filas, min_columnas) 
    num_barcos = random.randint(num_barcos, min(n, m))

    tablero = generar_tablero(n, m) # O(n*m)

    max_barcos = min(4, num_barcos)
    restricciones_filas, restricciones_columnas = restricciones_aleatorias(n, m, max_barcos) # O(n+m)

    longitudes_barcos_colocados = generar_barcos(tablero, restricciones_filas, restricciones_columnas, num_barcos) # O(n*m)

    return restricciones_filas, restricciones_columnas, longitudes_barcos_colocados

# O(n*m)