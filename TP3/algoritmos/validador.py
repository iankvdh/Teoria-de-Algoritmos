"""
Validador de soluciones para el juego de la batalla naval. Dado un tablero de dimensiones n x m, una lista de restricciones
para las filas y columnas, y una lista de barcos con sus posiciones y orientaciones, este algoritmo verifica si la solución
propuesta es válida. Para ser válida, la solución debe cumplir con las restricciones de filas y columnas, y no debe haber barcos
adyacentes. Si la solución es válida, el algoritmo devuelve True, de lo contrario, devuelve False.
"""

HORIZONTAL = "horizontal"
VERTICAL = "vertical"
BARCO = 1

def validador(n, m, restricciones_filas, restricciones_columnas, barcos):  #barcos = [1,3,'horizontal', 4]
    tablero_solucion = [[0] * m for _ in range(n)]                         #[fila, columna, orientacion, longitud]

    pos_barcos = []

    for barco in barcos:
        set_barco = set()
        fila, columna, orientacion, longitud = barco
        # Verificar si el barco cabe en el tablero en la dirección especificada
        if orientacion == HORIZONTAL and columna + longitud <= m:
            for i in range(longitud):
                tablero_solucion[fila][columna + i] = BARCO
                set_barco.add((fila, columna + i))
        elif orientacion == VERTICAL and fila + longitud <= n:
            for i in range(longitud):
                tablero_solucion[fila + i][columna] = BARCO
                set_barco.add((fila + i, columna))
        else:
            print(f"Error: el barco en posición ({fila}, {columna}) con orientación {orientacion} y longitud {longitud} se sale del tablero.")
            continue

        pos_barcos.append(set_barco)

    # restricciones filas
    for i in range(n):
        ocupados_en_fila = sum(tablero_solucion[i])
        if ocupados_en_fila != restricciones_filas[i]:
            return False

    # restricciones columnas
    for j in range(m):
        ocupados_en_columna = 0
        for i in range(n):
            if tablero_solucion[i][j] == BARCO:
                ocupados_en_columna += 1
        if ocupados_en_columna != restricciones_columnas[j]:
            return False

    # restricciones adyacencias
    for i, set_barco in enumerate(pos_barcos):
        for (fila, col) in set_barco:
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                ni, nj = fila + dx, col + dy
                # Si la posición adyacente está dentro del tablero
                if 0 <= ni < n and 0 <= nj < m:
                    # Verificamos si esta posición pertenece a otro barco
                    for j, otro_barco in enumerate(pos_barcos):
                        if j != i and (ni, nj) in otro_barco:
                            return False

    return True

"""
n = 10
m = 10
restricciones_filas = [3,2,2,4,2,1,1,2,3,0]
restricciones_columnas = [1,2,1,3,2,2,3,1,5,0]
barcos = [ # (fila, columna, orientación, longitud) basado en el diagrama del enunciado
    (0, 4, 'horizontal', 3),
    (1, 0, 'horizontal', 1),
    (1, 8, 'horizontal', 1),
    (2, 2, 'horizontal', 2),
    (3, 5, 'horizontal', 4),
    (4, 1, 'vertical', 2),
    (6, 8, 'vertical', 3),
    (7, 6, 'vertical', 1),
    (8, 3, 'horizontal', 2),
    (4, 3, 'horizontal', 1)
]

es_valido = validador(n, m, restricciones_filas, restricciones_columnas, barcos)
print("¿La configuración es válida?", es_valido)
"""