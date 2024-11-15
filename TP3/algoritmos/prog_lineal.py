import pulp

def definir_variables(n, m, barco_largos):
    x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(m)), cat="Binary")
    d = pulp.LpVariable.dicts("d", (i for i in range(n)), lowBound=0, cat="Continuous")
    e = pulp.LpVariable.dicts("e", (j for j in range(m)), lowBound=0, cat="Continuous")
    y = pulp.LpVariable.dicts("y", (k for k in range(len(barco_largos))), cat="Binary")
    return x, d, e, y

def definir_funcion_objetivo(problema, d, e, n, m):
    # Minimizar la demanda incumplida total en filas y columnas
    problema += pulp.lpSum(d[i] for i in range(n)) + pulp.lpSum(e[j] for j in range(m)), "Demanda_Incumplida_Total"

def agregar_restricciones(problema, x, d, e, y, n, m, barco_largos, demanda_filas, demanda_columnas):
    # Restricciones de demanda por fila
    for i in range(n):
        problema += (pulp.lpSum(x[i, j] for j in range(m)) + d[i] == demanda_filas[i]), f"Demanda_Fila_{i}"

    # Restricciones de demanda por columna
    for j in range(m):
        problema += (pulp.lpSum(x[i, j] for i in range(n)) + e[j] == demanda_columnas[j]), f"Demanda_Columna_{j}"

    # Restricciones de ubicación de los barcos
    for k, largo in enumerate(barco_largos):
        for i in range(n):
            for j in range(m):
                if i + largo <= n:
                    problema += pulp.lpSum(x[i + l, j] for l in range(largo)) <= y[k]
                if j + largo <= m:
                    problema += pulp.lpSum(x[i, j + l] for l in range(largo)) <= y[k]

def imprimir_resultados(problema, x, d, e, n, m):

    for i in range(n):
        fila = ""
        for j in range(m):
            if pulp.value(x[i, j]) == 1:
                fila += "B "  # 'B' representa una casilla ocupada por un barco
            else:
                fila += ". "  # '.' representa una casilla vacía
        print(fila)

    print("\nDemanda incumplida en filas:")
    for i in range(n):
        print(f"Fila {i+1}: {pulp.value(d[i])} casillas.")

    print("\nDemanda incumplida en columnas:")
    for j in range(m):
        print(f"Columna {j+1}: {pulp.value(e[j])} casillas.")

def resolver_batalla_naval(barco_largos, demanda_filas, demanda_columnas):
    n = len(demanda_filas)
    m = len(demanda_columnas)
    problema = pulp.LpProblem("Batalla_Naval", pulp.LpMinimize)

    x, d, e, y = definir_variables(n, m, barco_largos)

    definir_funcion_objetivo(problema, d, e, n, m)

    agregar_restricciones(problema, x, d, e, y, n, m, barco_largos, demanda_filas, demanda_columnas)

    problema_resuelto = problema.solve()

    imprimir_resultados(problema_resuelto, x, d, e, n, m)


def main():
    barco_largos = [3, 2, 2]
    demanda_filas = [3, 3, 2, 2, 1]
    demanda_columnas = [2, 3, 2, 2, 1]
    
    resolver_batalla_naval(barco_largos, demanda_filas, demanda_columnas) 
    # DEBERIAMOS AGREGAR UNA RESTRICCION DE QUE CADA BARCO DEBE ESTAR EN UNA SOLA FILA O COLUMNA

if __name__ == "__main__":
    main()