from pulp import LpMaximize, LpProblem, LpVariable, lpSum


# Parámetros
demandas_filas = [0, 3, 4, 1, 1, 4, 5, 0, 4, 5, 4, 2, 4, 3, 2]
demandas_columnas = [0, 0, 3, 4, 1, 4, 6, 5, 2, 0]
barcos = [6, 2, 1, 8, 7, 2, 7, 2, 5, 8, 1, 8, 8, 1, 6]

#demandas_filas  = [3,3,0,1,1]  # Demandas de filas
#demandas_columnas  = [3,1,0,3,3]  # Demandas de columnas
#barcos = [1,2,2,2,2,1]  # Lista de barcos por tamaño


def batalla_naval(demandas_filas, demandas_columnas, barcos):
    n = len(demandas_filas) 
    m = len(demandas_columnas)  
    k = len(barcos)  

    model = LpProblem("Maximizar_demanda_cumplida", LpMaximize)

    # Variables
    barco_usado = [LpVariable(f"barco_usado_{i}", cat="Binary") for i in range(k)]
    
    inicio_horizontal = [
        [[LpVariable(f"inicio_hor_{i}_{x}_{y}", cat="Binary") for y in range(m)] for x in range(n)]
        for i in range(k)
    ]
    
    inicio_vertical = [
        [[LpVariable(f"inicio_ver_{i}_{x}_{y}", cat="Binary") for y in range(m)] for x in range(n)]
        for i in range(k)
    ]

    # Restricción: Cada barco puede estar horizontal o vertical, pero no ambas
    for i in range(k):
        model += lpSum(inicio_horizontal[i][x][y] + inicio_vertical[i][x][y] 
                       for x in range(n) for y in range(m)) <= barco_usado[i]

    # Restricciones de no adyacencia (entre barcos diferentes)
    for i in range(k):  # Barco i
        for x in range(n):
            for y in range(m):
                # Si el barco i ocupa (x, y), no puede haber barcos distintos adyacentes
                casillero_ocupado_i = lpSum(
                    inicio_horizontal[i][x][y1]
                    for y1 in range(max(0, y - barcos[i] + 1), min(y + 1, m))
                ) + lpSum(
                    inicio_vertical[i][x1][y]
                    for x1 in range(max(0, x - barcos[i] + 1), min(x + 1, n))
                )

                # Restricciones para los casilleros vecinos de (x, y)
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m:  # Vecino dentro del tablero
                        # Casillero ocupado por cualquier barco (excluyendo i)
                        casillero_ocupado_otros = lpSum(
                            inicio_horizontal[j][nx][ny1]
                            for j in range(k) if j != i
                            for ny1 in range(max(0, ny - barcos[j] + 1), min(ny + 1, m))
                        ) + lpSum(
                            inicio_vertical[j][nx1][ny]
                            for j in range(k) if j != i
                            for nx1 in range(max(0, nx - barcos[j] + 1), min(nx + 1, n))
                        )

                        # Prohibir adyacencias entre barco i y cualquier otro barco
                        model += casillero_ocupado_i + casillero_ocupado_otros <= 1


    # Restricción: No superar demandas de filas
    for x in range(n):
        # Contribución horizontal
        contrib_horizontal = lpSum(
            barcos[i] * inicio_horizontal[i][x][y] 
            for i in range(k) for y in range(m - barcos[i] + 1)
        )
        
        # Contribución vertical
        contrib_vertical = lpSum(
            barcos[i] * inicio_vertical[i][x1][y] 
            for i in range(k) for y in range(m) 
            for x1 in range(max(0, x - barcos[i] + 1), min(x + 1, n)) 
        )
        
        # Restricción para la fila x
        model += contrib_horizontal + contrib_vertical <= demandas_filas[x]


    # Restricción: No superar demandas de columnas
    for y in range(m):
        contrib_horizontal = lpSum(
            barcos[i] * inicio_horizontal[i][x][y] 
            for i in range(k) for x in range(n) 
            for y1 in range(max(0, y - barcos[i] + 1), min(y + 1, m))
        )
        
        contrib_vertical = lpSum(
            barcos[i] * inicio_vertical[i][x][y] 
            for i in range(k) for x in range(n - barcos[i] + 1)
        )
        
        model += contrib_horizontal + contrib_vertical <= demandas_columnas[y]


    # Restricción: Un barco por casillero (unicidad)
    for x in range(n):
        for y in range(m):
            # Casillero ocupado por barcos horizontales
            contrib_horizontal = lpSum(
                inicio_horizontal[i][x][y1]
                for i in range(k)
                for y1 in range(max(0, y - barcos[i] + 1), min(y + 1, m))  # Casillas ocupadas por horizontales
            )
            
            # Casillero ocupado por barcos verticales
            contrib_vertical = lpSum(
                inicio_vertical[i][x1][y]
                for i in range(k)
                for x1 in range(max(0, x - barcos[i] + 1), min(x + 1, n))  # Casillas ocupadas por verticales
            )
            
            # Restricción de unicidad por casillero
            model += contrib_horizontal + contrib_vertical <= 1


    # Función objetivo: Maximizar la demanda cumplida
    model += lpSum(barcos[i] * (lpSum(inicio_horizontal[i][x][y] + inicio_vertical[i][x][y]
                                      for x in range(n) for y in range(m))) for i in range(k))


    model.solve()

    # Extraer solución
    posiciones = []
    for i in range(k):
        colocado = False
        for x in range(n):
            for y in range(m):
                if inicio_horizontal[i][x][y].varValue == 1:
                    posiciones.append(((x, y), (x, y + barcos[i] - 1)))
                    colocado = True
                    break
                elif inicio_vertical[i][x][y].varValue == 1:
                    posiciones.append(((x, y), (x + barcos[i] - 1, y)))
                    colocado = True
                    break
            if colocado:
                break
        if not colocado:
            posiciones.append(None)

    demanda_cumplida = sum(demandas_filas) + sum(demandas_columnas)
    demanda_total = 2 * sum(barcos)

    return posiciones, demanda_cumplida, demanda_total



posiciones, demanda_cumplida, demanda_total = batalla_naval(demandas_filas, demandas_columnas, barcos)
print("Posiciones seleccionadas para los barcos:", posiciones)
print("Demanda cumplida esperada:", demanda_cumplida)
print("Demanda total:", demanda_total)



# Función para imprimir el tablero con los barcos colocados
def print_barcos(barcos, lista_pos, demandas_filas, demandas_columnas):

    n = len(demandas_filas)  # Número de filas
    m = len(demandas_columnas)  # Número de columnas
    matriz = [[None for _ in range(m)] for _ in range(n)]
    for i, pos in enumerate(lista_pos):
        if pos:
            (x1, y1), (x2, y2) = pos
            if x1 == x2:  # Horizontal
                for y in range(y1, y2 + 1):
                    matriz[x1][y] = str(i)
            else:  # Vertical
                for x in range(x1, x2 + 1):
                    matriz[x][y1] = str(i)
    for fila in matriz:
        print(fila)

print_barcos(barcos, posiciones, demandas_filas, demandas_columnas)
