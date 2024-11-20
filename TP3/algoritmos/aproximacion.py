from algoritmos.leer_archivos import leer_inputs

VACIO = "-"

# recibe las restricciones de filas y columnas y las transforma en una lista de tuplas (idx, demanda, es_fila/es_columna)
def transoformar_restricciones(restricciones_filas, restricciones_columnas):
    restricciones_filas_con_idx = []
    restricciones_columnas_con_idx = []
    for i, restriccion in enumerate(restricciones_filas):
        tupla = i, restriccion, True
        restricciones_filas_con_idx.append(tupla)
    for j, restriccion in enumerate(restricciones_columnas):
        tupla = j, restriccion, False
        restricciones_columnas_con_idx.append(tupla)
    return restricciones_filas_con_idx + restricciones_columnas_con_idx

def aproximacion(tablero, restricciones_filas, restricciones_columnas, barcos):
    
    restricciones = transoformar_restricciones(restricciones_filas, restricciones_columnas)
    n = len(restricciones_filas)
    m = len(restricciones_columnas)
    restricciones.sort(key=lambda x: x[1], reverse=True)
    barcos.sort(reverse=True)
    barco_actual = 0
    demanda_restante_filas = restricciones_filas[:]
    demanda_restante_columnas = restricciones_columnas[:]
    pude_poner = False
    for restriccion in restricciones:
        idx, demanda, es_fila = restriccion
        pude_poner = False
        if not barcos:
            break
        largo_barco = barcos.pop(0)
        # Ir a fila/columna de mayor demanda, 
        while not pude_poner:
            if es_fila:
                idx_fila = idx
                for j in range(m):
                    # y ubicar el barco de mayor longitud en dicha fila/columna en algún lugar válido. 
                    # Si el barco de mayor longitud es más largo que dicha demanda, simplemente saltearlo y seguir con el siguiente. 
                    
                    if entra_en_el_tablero(tablero, idx_fila, j, largo_barco, 0) \
                        and not exede_demanda(idx_fila, j, largo_barco, 0, demanda_restante_filas, demanda_restante_columnas) \
                        and not tiene_adyacentes(tablero, idx_fila, j, largo_barco, 0, n, m):
                        tablero, demanda_restante_filas, demanda_restante_columnas = colocar_barco(tablero, idx_fila, j, 0, largo_barco, barco_actual, demanda_restante_filas, demanda_restante_columnas)
                        barco_actual += 1
                        pude_poner = True    
                        break
            else:
                idx_col = idx
                for i in range(n):

                    if entra_en_el_tablero(tablero, i, idx_col, largo_barco, 1) \
                        and not exede_demanda(i, idx_col, largo_barco, 1, demanda_restante_filas, demanda_restante_columnas) \
                        and not tiene_adyacentes(tablero, i, idx_col, largo_barco, 1, n, m):
                        tablero, demanda_restante_filas, demanda_restante_columnas = colocar_barco(tablero, i, idx_col, 1, largo_barco, barco_actual, demanda_restante_filas, demanda_restante_columnas)
                        barco_actual += 1
                        pude_poner = True    
                        break
            if not barcos:
                break
            largo_barco = barcos.pop(0)
            


def entra_en_el_tablero(tablero, fila, col, largo, orientacion):
        try:
            if orientacion == 0:  # Horizontal
                return all(tablero[fila][j] == VACIO for j in range(col, col + largo))
            else:  # Vertical
                return all(tablero[i][col] == VACIO for i in range(fila, fila + largo))
        except IndexError:
            return False

def exede_demanda(fila, col, largo, orientacion, demanda_restante_filas, demanda_restante_columnas):
    if orientacion == 0:  # Horizontal
        if demanda_restante_filas[fila] < largo:
            return True
        if any(demanda_restante_columnas[j] < 1 for j in range(col, col + largo)):
            return True
    else:  # Vertical
        if demanda_restante_columnas[col] < largo:
            return True
        if any(demanda_restante_filas[i] < 1 for i in range(fila, fila + largo)):
            return True
    return False

def tiene_adyacentes(tablero, fila, col, largo, orientacion, n, m):
    if orientacion == 0:  # Horizontal
        for j in range(col - 1, col + largo + 1):
            if not (0 <= j < m):
                continue
            for i in [fila - 1, fila, fila + 1]:
                if 0 <= i < n and tablero[i][j] != VACIO:
                    return True
    else:  # Vertical
        for i in range(fila - 1, fila + largo + 1):
            if not (0 <= i < n):
                continue
            for j in [col - 1, col, col + 1]:
                if 0 <= j < m and tablero[i][j] != VACIO:
                    return True
    return False


def colocar_barco(tablero, fila, col, orientacion, largo, ship_indice, demanda_restante_filas, demanda_restante_columnas):
    if orientacion == 0:  # Horizontal
        for j in range(col, col + largo):
            tablero[fila][j] = str(ship_indice)
            demanda_restante_columnas[j] -= 1
        demanda_restante_filas[fila] -= largo
    else:  # Vertical
        for i in range(fila, fila + largo):
            tablero[i][col] = str(ship_indice)
            demanda_restante_filas[i] -= 1
        demanda_restante_columnas[col] -= largo
    return tablero, demanda_restante_filas, demanda_restante_columnas

def print_solution(demandas_filas, demandas_columnas, mejor_tablero):
    n = len(demandas_filas)
    m = len(demandas_columnas)
    restricciones_columnas = [" ", " "] + [str(c) + " " for c in demandas_columnas]
    print(''.join(restricciones_columnas))
    for i in range(n):
        fila_str = [str(demandas_filas[i]) + " "] + [mejor_tablero[i][j] + " " for j in range(m)]
        print(''.join(fila_str))
    print()

def print_demanda_cumplida(tablero):
    n = len(tablero)
    m = len(tablero[0])
    cant = 0
    for i in range(n):
        for j in range(m):
            if tablero[i][j] != VACIO:
                cant+=1
    print("Demanda total cumplida: ", cant*2)
    
def mostrar_resultados_ruta_abs_aprox(ruta_abs):
    demandas_filas, demandas_columnas, barcos = leer_inputs(ruta_abs)
    n = len(demandas_filas)
    m = len(demandas_columnas)
    tablero = [[VACIO for _ in range(m)] for _ in range(n)]
    aproximacion(tablero, demandas_filas, demandas_columnas, barcos)
    print_solution(demandas_filas, demandas_columnas, tablero)
    print_demanda_cumplida(tablero)
    