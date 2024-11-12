HORIZONTAL = "horizontal"
VERTICAL = "vertical"
BARCO = 1

def validador(n, m, restricciones_filas, restricciones_columnas, barcos):
    tablero_solucion = [[0] * m for _ in range(n)] 

    pos_barcos = []

    for barco in barcos:
        set_barco = set()
        fila, columna, orientacion, longitud = barco

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
                if 0 <= ni < n and 0 <= nj < m:
                    for j, otro_barco in enumerate(pos_barcos):
                        if j != i and (ni, nj) in otro_barco:
                            return False

    return True
