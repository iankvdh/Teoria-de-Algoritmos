# algoritmo de aproximación: 
# Ir a fila/columna de mayor demanda, y ubicar el barco de mayor longitud en dicha fila/columna en algún lugar válido. 
# Si el barco de mayor longitud es más largo que dicha demanda, simplemente saltearlo y seguir con el siguiente. 
# Volver a aplicar hasta que no queden más barcos o no haya más demandas a cumplir. 
# 
# Este algoritmo sirve como una aproximación para resolver el problema de La Batalla Naval. 
# Implementar dicho algoritmo, analizar su complejidad y analizar cuán buena aproximación es. 
# Para esto, considerar lo siguiente: 
# Sea I una instancia cualquiera del problema de La Batalla Naval, 
# y z(I) una solución óptima para dicha instancia, 
# y sea A(I) la solución aproximada, 
# se define  A(I)/z(I)≤r(A) para todas las instancias posibles. 
# Calcular  r(A) para el algoritmo dado, demostrando que la cota está bien calculada. 
# 
# Realizar mediciones utilizando el algoritmo exacto y la aproximación, con el objetivo de verificar dicha relación. 
# Realizar también mediciones que contemplen volúmenes de datos ya inmanejables para el algoritmo exacto, 
# a fin de corroborar empíricamente la cota calculada anteriormente.


from leer_archivos import leer_inputs

VACIO = "-"
ES_FILA = 0
ES_COLUMNA = 1

archivo = '10_10_10.txt'

demandas_filas, demandas_columnas, barcos = leer_inputs('../data/' + archivo)
n = len(demandas_filas)
m = len(demandas_columnas)
tablero = [[VACIO for _ in range(m)] for _ in range(n)]


# recibe las restricciones de filas y columnas y las transforma en una lista de tuplas (idx, demanda, es_fila/es_columna)
def transoformar_restricciones(restricciones_filas, restricciones_columnas):
    restricciones_filas_con_idx = []
    restricciones_columnas_con_idx = []
    for i, restriccion in enumerate(restricciones_filas):
        tupla = i, restriccion, ES_FILA
        restricciones_filas_con_idx.append(tupla)
    for j, restriccion in enumerate(restricciones_columnas):
        tupla = j, restriccion, ES_COLUMNA
        restricciones_columnas_con_idx.append(tupla)
    return restricciones_filas_con_idx + restricciones_columnas_con_idx

def aproximacion(tablero, restricciones_filas, restricciones_columnas, barcos):
    
    restricciones = transoformar_restricciones(restricciones_filas, restricciones_columnas)
    n = len(restricciones_filas)
    m = len(restricciones_columnas)
    restricciones.sort(key=lambda x: x[1], reverse=True)
    barcos.sort(reverse=True)

    for restriccion in restricciones:
        idx, demanda, es_fila = restriccion
        largo_barco = barcos.pop(0)
        if not barcos:
            break
        # Ir a fila/columna de mayor demanda, 
        if es_fila:
            for i in range(n):
                # y ubicar el barco de mayor longitud en dicha fila/columna en algún lugar válido. 
                # Si el barco de mayor longitud es más largo que dicha demanda, simplemente saltearlo y seguir con el siguiente. 
                if idx == 6:
                    print(i, idx)
                if not es_posicion_valida(tablero, idx, i, demanda, largo_barco, es_fila):
                    continue
                for j in range(demanda):
                    tablero[i][j] = str(idx)                
                break
        else:
            for j in range(m):
                if not es_posicion_valida(tablero, j, idx, demanda, largo_barco, es_fila):
                    continue
                for i in range(demanda):
                    tablero[i][j] = str(idx)
                break

def es_posicion_valida(tablero, i, j, demanda, largo_barco, es_fila):
    if es_fila:
        # el barco ya no entra
        if j + largo_barco > m:
            return False
        # si hay algo en el camino
        if i == 6:
            print(i, j)

        for k in range(j, j + largo_barco):
            if tablero[i][k] != VACIO:
                return False
        # adyacencias
        if j > 0 and tablero[i][j - 1] != VACIO:
            return False
        if j + largo_barco < m and tablero[i][j + largo_barco] != VACIO:
            return False
        
        # sumar la demanda que ya hay cumplida en esa fila
        demanda_actual = 0
        for k in range(m):
            if tablero[i][k] != VACIO:
                demanda_actual += 1
        if demanda_actual + largo_barco > demanda:
            return False
    else:
        # el barco ya no entra
        if i + largo_barco > n:
            return False
        # si hay algo en el camino
        for k in range(i, i + largo_barco):
            if tablero[k][j] != VACIO:
                return False
        # adyacencias
        if i > 0 and tablero[i - 1][j] != VACIO:
            return False
        if i + largo_barco < n and tablero[i + largo_barco][j] != VACIO:
            return False
        
        # sumar la demanda que ya hay cumplida en esa columna
        demanda_actual = 0
        for k in range(n):
            if tablero[k][j] != VACIO:
                demanda_actual += 1
        if demanda_actual + largo_barco > demanda:
            return False
        
    return True

aproximacion(tablero, demandas_filas, demandas_columnas, barcos)


def print_solution(demandas_filas, demandas_columnas, mejor_tablero):
    n = len(demandas_filas)
    m = len(demandas_columnas)
    restricciones_columnas = [" ", " "] + [str(c) + " " for c in demandas_columnas]
    print(''.join(restricciones_columnas))
    for i in range(n):
        fila_str = [str(demandas_filas[i]) + " "] + [mejor_tablero[i][j] + " " for j in range(m)]
        print(''.join(fila_str))
    print()

print_solution(demandas_filas, demandas_columnas, tablero)