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

FACTOR_TIEMPO = 1000 # milisegundos

def modelo_lineal(x, m, b):
    return m * x + b

def modelo_cuadratico(x, a, b, c):
    return a * x**2 + b * x + c

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


def configurar_posiciones_barcos(posiciones):
    posiciones_resultantes = []
    for pos in posiciones:
        if pos is None:  # Si es None, se agrega tal cual
            posiciones_resultantes.append(None)
        elif isinstance(pos, tuple) and len(pos) == 2 and isinstance(pos[0], tuple):  # Si es un rango
            start, end = pos
            if start[0] == end[0]:  # Barco horizontal (misma fila)
                posiciones_resultantes.append([(start[0], y) for y in range(start[1], end[1] + 1)])
            elif start[1] == end[1]:  # Barco vertical (misma columna)
                posiciones_resultantes.append([(x, start[1]) for x in range(start[0], end[0] + 1)])
        elif isinstance(pos, tuple):  # Posición única
            posiciones_resultantes.append([pos])
    return posiciones_resultantes
