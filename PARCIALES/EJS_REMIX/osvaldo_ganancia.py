"""
Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso. Está viendo cómo se predice que evolucionará el precio de un inmueble (el cual no poseen, pero pueden comprar). Tiene la información de estas predicciones en el arreglo p, para todo día i = 1, 2, ..., n. Osvaldo quiere determinar un día j en el cual comprar la casa, y un día k en el cual venderla (k > j), suponiendo que eso sucederá sin lugar a dudas. El objetivo, por supuesto, es la de maximizar la ganancia dada por p[k] - p[j].
"""

# OP1: POR PROGRAMACION DINAMICA

# OPT(n): MAX[ OPT(n-1),  p[n] - min(p[1:n-1]) ]
def ganancia_osvaldo_pd(p):
    n = len(p)

    # caso base
    if n < 2:
        return None, None
    
    # memo: [(ult_min, diferencia)]
    memo = [(0, 0)] * (n)
    memo[0] = (p[0], 0)

    if p[1] - p[0] >= 0:
        memo[1] = (min(p[0], p[1]), p[1] - p[0])
    else: 
        memo[1] = (min(p[0], p[1]), 0)

    for i in range(2, n):
        valor_min = 0
        if p[i] < memo[i-1][0]:
            valor_min = p[i]
        else:
            valor_min = memo[i-1][0]
        memo[i] = (valor_min, max(memo[i-1][1], p[i] - memo[i-1][0]))
        
    return reconstruir(p, memo)

def reconstruir(p, memo):
    i = len(p) - 1
    dia_venta = len(p) - 1

    while i >= 0:
        if memo[i][1] != memo[dia_venta][1]:
            break
        dia_venta = i
        i -= 1
    # a este punto tengo mi dia de venta listo.

    while memo[dia_venta][0] != p[i]: 
        i -= 1
    # a este punto i es el dia de la compra

    return (i, dia_venta)

# OP2: POR DIVIDE AND CONQUER

def osvaldo_dyq(arr): # O(n log n)
    _, _, solucion = _osvaldo_dyq(arr, 0, len(arr) - 1)
    return solucion
    
def _osvaldo_dyq(arr, inicio, fin):
    if inicio == fin:
        # min, max, ganancia
        return inicio, inicio, (inicio, fin)
    
    mitad = (inicio + fin) // 2
    
    i_min_izq, i_max_izq, indices_ganancia_izq = _osvaldo_dyq(arr, inicio, mitad)
    i_min_der, i_max_der, indices_ganancia_der = _osvaldo_dyq(arr, mitad + 1, fin)
    
    ganancia_cruzada = arr[i_max_der] - arr[i_min_izq]
    ganancia_cruzada_indices = (i_min_izq, i_max_der)

    min_global = 0
    max_global = 0

    if arr[i_min_izq] < arr[i_min_der]:
        min_global = i_min_izq
    else:
        min_global = i_min_der

    if arr[i_max_izq] > arr[i_max_der]:
        max_global = i_max_izq
    else:
        max_global = i_max_der
    
    ganancia_izq = arr[indices_ganancia_izq[1]] - arr[indices_ganancia_izq[0]]
    ganancia_der = arr[indices_ganancia_der[1]] - arr[indices_ganancia_der[0]]
    
    if ganancia_cruzada >= ganancia_izq and ganancia_cruzada >= ganancia_der:
        return min_global, max_global, ganancia_cruzada_indices
    
    if ganancia_izq >= ganancia_der:
        return min_global, max_global, indices_ganancia_izq
    
    return min_global, max_global, indices_ganancia_der

# OP3: POR GREEDY

# recorro el arreglo una sola vez y voy guardando el minimo y el maximo
def osvaldo_greedy(p):
    n = len(p)
    minimo = p[0]
    maximo = p[1]
    minimo_indice = 0
    maximo_indice = 1
    ganancia = p[1] - p[0]

    for i in range(1, n):
        if p[i] - minimo > ganancia:
            ganancia = p[i] - minimo
            maximo = p[i]
            maximo_indice = i

        if p[i] < minimo:
            minimo = p[i]
            minimo_indice = i

    return minimo_indice, maximo_indice

"""
Es un algoritmo greedy porque en cada paso toma la mejor decision local, que es comprar en el minimo y vender en el maximo de los valores que se han visto hasta el momento.
"""

# OP4: POR BACKTRACKING

# No tiene mucho sentido xd

# OP5: POR PROGRAMACION LINEAL

"""
Planteamos que tenemos una variable:

V_i: variable binaria de "vendo el día i"
C_i: variable binaria de "compro el día i"

Solo compramos y vendemos un día:
sum V_i = 1
sum C_i = 1

Ahora tenemos que ver que si o si compremos antes que vendamos. Eso se resuelve obteniendo primero qué día es que compramos y vendemos:

C_ef: variable entera que indica qué día compramos
V_ef: variable entera que indica que día vendemos
C_ef = sum i * C_i
V_ef = sum i * V_i

Y ahora podemos ver que se venda luego:
C_ef < V_ef

Esto último se puede hacer sin pasar por estas variables auxiliares, haciendo directo:
sum i * C_i < sum i * V_i

Esto es claridad vs. tener menos variables y ecuaciones (2 y 2 en cada caso, no es representativo). En cualquier caso ambas las tomamos como bien.

Último paso, qué queremos optimizar:
max [ sum (p[i] * V_i) - sum (p[i] C_i) ]
"""
