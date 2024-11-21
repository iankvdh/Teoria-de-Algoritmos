from pulp import LpMinimize, LpProblem, LpVariable, lpSum

# Parámetros
#demandas_filas = [0, 3, 4, 1, 1, 4, 5, 0, 4, 5, 4, 2, 4, 3, 2]
#demandas_columnas = [0, 0, 3, 4, 1, 4, 6, 5, 2, 0]
#barcos = [6, 2, 1, 8, 7, 2, 7, 2, 5, 8, 1, 8, 8, 1, 6]

demandas_filas  = [3,3,0,1,1]  # Demandas de filas
demandas_columnas  = [3,1,0,3,3]  # Demandas de columnas
barcos = [1,2,2,2,2,1]  # Lista de barcos por tamaño


def batalla_naval(demandas_filas, demandas_columnas, barcos):
    print("Demandas de filas: ", demandas_filas)
    print("Demandas de columnas: ", demandas_columnas)
    print("Barcos: ", barcos)
    print(len(barcos))
    n = len(demandas_filas)  # Número de filas
    m = len(demandas_columnas)  # Número de columnas
    k = len(barcos)  # Número de barcos

    # Variables de decisión
    Yh = {i: LpVariable(f"Yh_{i}", cat="Binary") for i in range(k)}  # Barco i en horizontal
    Yv = {i: LpVariable(f"Yv_{i}", cat="Binary") for i in range(k)}  # Barco i en vertical
    Pos_fila_i = {i: LpVariable(f"Pos_fila_i_{i}", lowBound=0, cat="Integer") for i in range(k)}  # Fila de inicio del barco i
    Pos_col_i = {i: LpVariable(f"Pos_col_i_{i}", lowBound=0, cat="Integer") for i in range(k)}  # Columna de inicio del barco i

    # Variables auxiliares
    demandas_no_cumplidas_fila = {x: LpVariable(f"demanda_no_cumplida_fila_{x}", lowBound=0, cat="Integer") for x in range(n)}  # Demanda no cumplida en la fila x
    for x in range(n):
        demandas_no_cumplidas_fila[x].setInitialValue(demandas_filas[x])  # Inicializar las demandas no cumplidas en las filas
    demandas_no_cumplidas_col = {y: LpVariable(f"demanda_no_cumplida_col_{y}", lowBound=0, cat="Integer") for y in range(m)}  # Demanda no cumplida en la columna y
    for y in range(m):
        demandas_no_cumplidas_col[y].setInitialValue(demandas_columnas[y]) # Inicializar las demandas no cumplidas en las columnas

    # Función objetivo
    model = LpProblem("Minimizar_demanda_no_cumplida", LpMinimize)
    model += lpSum([demandas_no_cumplidas_fila[x] for x in range(n)]) + lpSum([demandas_no_cumplidas_col[y] for y in range(m)])

    # Restricciones
    # 1. Cada barco puede estar horizontal o vertical, pero no ambas, puedo no ponerlo (esto esta bien)
    for i in range(k):
        model += Yh[i] + Yv[i] <= 1

    # 2. Las posiciones de los barcos deben estar dentro del tablero (esto esta bien)
    for i in range(k):
        model += Pos_fila_i[i] + barcos[i] * Yh[i] <= n 
        model += Pos_col_i[i] + barcos[i] * Yv[i] <= m 

    
    # Cumplir demandas de filas (esto esta bien)
    for x in range(n):
        model += lpSum([Yh[i] * barcos[i] for i in range(k) if Pos_fila_i[i] == x]) + lpSum(Yv[i] for i in range(k) if Pos_fila_i[i] == x) + demandas_no_cumplidas_fila[x] == demandas_filas[x]
        
    # Cumplir demandas de columnas (esto esta bien)
    for y in range(m):
        model += lpSum([Yv[i] * barcos[i] for i in range(k) if Pos_col_i[i] == y]) + lpSum(Yh[i] for i in range(k) if Pos_col_i[i] == y) + demandas_no_cumplidas_col[y] == demandas_columnas[y]
    
    # 5. Restricciones de no superposicion de barcos


    # 6. Restricciones de adyacencia entre barcos (no pueden haber barcos al rededor de un barco)


    # Resolver el problema
    model.solve()

    # Imprimir resultados
    posiciones = [] # Lista de posiciones de los barcos [((inicio_fila, inicio_col), (fin_fila, fin_col)), ...] para k barcos
    for i in range(k):
        # si no lo coloco, pongo None
        print(f'Yh_{i}: {Yh[i].value()}')
        print(f'Yv_{i}: {Yv[i].value()}')
        if Yh[i]:
            posiciones.append(((Pos_fila_i[i].value(), Pos_col_i[i].value()), (Pos_fila_i[i].value(), Pos_col_i[i].value() + barcos[i] - 1)))
        elif Yv[i]:
            posiciones.append(((Pos_fila_i[i].value(), Pos_col_i[i].value()), (Pos_fila_i[i].value() + barcos[i] - 1, Pos_col_i[i].value())))
        else:
            posiciones.append(None)

    return posiciones


def generar_matriz_obtenida(lista_pos, demandas_filas, demandas_columnas):
    n = len(demandas_filas)
    m = len(demandas_columnas)
    matriz = [[None for _ in range(m)] for _ in range(n)]
    # [None, ((0.0, 2.0), (0.0, 3.0)), ((0.0, 0.0), (0.0, 1.0)), ((0.0, 0.0), (1.0, 0.0)), ((0.0, 0.0), (0.0, 1.0)), ((0.0, 0.0), (0.0, 0.0))]
    # debo pasar todas las posiciones a enteros
    for i, pos in enumerate(lista_pos):
        if pos:
            (x1, y1), (x2, y2) = pos
            if x1 == x2:
                for y in range(int(y1), int(y2) + 1):
                    matriz[int(x1)][y] = str(i)
            else:
                for x in range(int(x1), int(x2) + 1):
                    matriz[x][int(y1)] = str(i)
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