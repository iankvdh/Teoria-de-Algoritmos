from pulp import LpMinimize, LpProblem, LpVariable, lpSum

# Parámetros
#demandas_filas = [0, 3, 4, 1, 1, 4, 5, 0, 4, 5, 4, 2, 4, 3, 2]
#demandas_columnas = [0, 0, 3, 4, 1, 4, 6, 5, 2, 0]
#barcos = [6, 2, 1, 8, 7, 2, 7, 2, 5, 8, 1, 8, 8, 1, 6]

demandas_filas  = [3,3,0,1,1]  # Demandas de filas
demandas_columnas  = [3,1,0,3,3]  # Demandas de columnas
barcos = [1,2,2,2,2,1]  # Lista de barcos por tamaño

def batalla_naval(demandas_filas, demandas_columnas, barcos):
    n = len(demandas_filas)  # Número de filas
    m = len(demandas_columnas)  # Número de columnas
    k = len(barcos)  # Número de barcos

    # Variables de decisión
    Yh = [LpVariable(f"Yh_{i}", cat="Binary") for i in range(k)]
    Yv = [LpVariable(f"Yv_{i}", cat="Binary") for i in range(k)]
    Pos_fila_i = [LpVariable(f"Pos_fila_{i}", lowBound=0, upBound=n - 1, cat="Integer") for i in range(k)]
    Pos_col_i = [LpVariable(f"Pos_col_{i}", lowBound=0, upBound=m - 1, cat="Integer") for i in range(k)]

    demanda_no_cumplida_fila = [LpVariable(f"demanda_no_cumplida_fila_{x}", lowBound=0, cat="Integer") for x in range(n)]
    demanda_no_cumplida_col = [LpVariable(f"demanda_no_cumplida_col_{y}", lowBound=0, cat="Integer") for y in range(m)]

    # Función objetivo
    model = LpProblem("Minimizar_demanda_no_cumplida", LpMinimize)
    model += lpSum(demanda_no_cumplida_fila) + lpSum(demanda_no_cumplida_col)

    # Restricciones
    # 1. Cada barco puede estar horizontal o vertical, pero no ambas, puedo no ponerlo (esto esta bien)
    for i in range(k):
        model += Yh[i] + Yv[i] <= 1

    # 2. Las posiciones de los barcos deben estar dentro del tablero (esto esta bien)
    for i in range(k):
        model += Pos_fila_i[i] + barcos[i] * Yv[i] <= n  # Vertical | Posi desde fila donde arranca + tamaño del barco * si es vertical <= n
        model += Pos_col_i[i] + barcos[i] * Yh[i] <= m  # Horizontal | Posi desde columna donde arranca + tamaño del barco * si es horizontal <= m

    # No superar demandas de filas (tomo la fila y sumo los barcos que estan en esa fila)
    for x in range(n):
        model += lpSum(barcos[i] * Yh[i] for i in range(k) if Pos_fila_i[i] == x) <= demandas_filas[x]

    # No superar demandas de columnas (tomo la columna y sumo los barcos que estan en esa columna)
    for y in range(m):
        model +=  lpSum((barcos[i] * Yv[i]) for i in range(k) if Pos_col_i[i] == y) <= demandas_columnas[y]
    
    # si hay un barco en la posición (x, y), entonces no puede haber otro barco en esa misma posición
    for i in range(k):
        # si alguna de las posiciones iniciales interseca con otra posición inicial, entonces no puede haber barco en esa posición
        for j in range(k):
            if i != j:
                model += Pos_fila_i[i] != Pos_fila_i[j] and Pos_col_i[i] != Pos_col_i[j]
    
    # si hay un barco en la posición (x, y), debo asegurarme de que no haya otro barco en las posiciones de su prolongación
    for i in range(k):
        if Yh[i].value() == 1:
            for j in range(barcos[i]):
                for l in range(k):
                    if l != i:
                        model += Pos_fila_i[i] + j != Pos_fila_i[l] and Pos_col_i[i] != Pos_col_i[l]
        if Yv[i].value() == 1:
            for j in range(barcos[i]):
                for l in range(k):
                    if l != i:
                        model += Pos_fila_i[i] != Pos_fila_i[l] and Pos_col_i[i] + j != Pos_col_i[l]

    # no deben haber barcos adyacentes a otro barco, para eso recorro todas las posiciones de los barcos prolongando su longitud
    # y me fijo que no choque con ninguna otra prolongación de barco
    for i in range(k):
        if Yh[i].value() == 1:
            for j in range(barcos[i]):
                for l in range(k):
                    if l != i:
                        for m in range(barcos[l]):
                            model += Pos_fila_i[i] + j != Pos_fila_i[l] and Pos_col_i[i] + j != Pos_col_i[l] + m

        if Yv[i].value() == 1:
            for j in range(barcos[i]):
                for l in range(k):
                    if l != i:
                        for m in range(barcos[l]):
                            model += Pos_fila_i[i] + j != Pos_fila_i[l] + m and Pos_col_i[i] + j != Pos_col_i[l]

    return model.solve()

    # Imprimir resultados
    posiciones = [] # Lista de posiciones de los barcos [((inicio_fila, inicio_col), (fin_fila, fin_col)), ...] para k barcos
    for i in range(k):
        # si no lo coloco, pongo None
        if Yh[i].value() == 0 and Yv[i].value() == 0:
            posiciones.append(None)
        if Yh[i].value() == 1:
            posiciones.append(((int(Pos_fila_i[i].value()), int(Pos_col_i[i].value())), (int(Pos_fila_i[i].value()), int(Pos_col_i[i].value() + barcos[i] - 1))))
        else:
            posiciones.append(((int(Pos_fila_i[i].value()), int(Pos_col_i[i].value())), (int(Pos_fila_i[i].value() + barcos[i] - 1), int(Pos_col_i[i].value()))))

    return posiciones


def generar_matriz_obtenida(lista_pos, demandas_filas, demandas_columnas):
    n = len(demandas_filas)
    m = len(demandas_columnas)
    matriz = [[None for _ in range(m)] for _ in range(n)]

    for i, pos in enumerate(lista_pos):
        if pos:
            (x1, y1), (x2, y2) = pos
            if x1 == x2:
                for y in range(y1, y2 + 1):
                    matriz[x1][y] = str(i)
            else:
                for x in range(x1, x2 + 1):
                    matriz[x][y1] = str(i)
    return matriz

def obtener_demanda_cumplida(matriz):
    n = len(matriz)
    m = len(matriz[0])
    demanda_cumplida = 0
    for i in range(n):
        for j in range(m):
            if matriz[i][j] != None:
                demanda_cumplida += 1
    return demanda_cumplida * 2

posiciones = batalla_naval(demandas_filas, demandas_columnas, barcos)
print("Posiciones obtenidas: ", posiciones)
matriz = generar_matriz_obtenida(posiciones, demandas_filas, demandas_columnas)
print("Matriz obtenida: ")
for fila in matriz:
    print(fila)
demandas_cumplidas = obtener_demanda_cumplida(matriz)
print("Demanda cumplida: ", demandas_cumplidas)