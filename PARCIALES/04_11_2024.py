# ------------------------ EJERCICIO 1 ------------------------
"""
Resolver, utilizando backtracking, el problema de la mochila con cantidades mínimas. Este tiene el mismo planteo al
original pero además cuenta con un parámetro K, donde además de las condiciones impuestas para el problema original,
se deben utilizar al menos K elementos. Es decir, el planteo completo es: Dados n elementos de valores v1, v2, ..., vn
con pesos p1, p2, ..., pn, y valores W y K, encontrar el subconjunto de al menos K elementos, cuya suma de valor sea
máxima y cuyo peso no exceda el valor de W.
"""
def k_mochila_min(elementos, W, k):
    """
    elementos: [(v1, p1), (v2, p2), ..., (vn, pn)]
    W: peso de la mochila
    k: cantidad de elementos, cuya suma de valor sea máxima y cuyo peso no exceda el valor W.
    """
    sol_parcial = []
    sol_optima = []
    return _k_mochila_min(elementos, W, k, 0, sol_optima, sol_parcial)

def _k_mochila_min(elementos, W, k, indice, sol_optima, sol_parcial):
    # caso base termino de iterar
    if len(elementos) == indice:
        if sumar_valores(sol_parcial) > sumar_valores(sol_optima):
            return sol_parcial[:] # O(n)
        return sol_optima[:] # O(n)

    # chequeo si la parcial es compatible (no se pasa de k, ni de W)
    sol_parcial.append(elementos[indice])
    if es_compatible(sol_parcial, W, k):
        sol_optima = _k_mochila_min(elementos, W, k, indice + 1, sol_optima, sol_parcial)

    sol_parcial.pop()
    return _k_mochila_min(elementos, W, k, indice + 1, sol_optima, sol_parcial)


def es_compatible(sol, W, k):
    if sumar_pesos(sol) > W:
        return False
    if sumar_cant_elementos(sol) > k:
        return False
    return True


# Funciones auxiliares
def sumar_cant_elementos(sol):
    res = 0
    for i in sol:
        res += 1
    return res

def sumar_valores(sol):
    res = 0
    for i in sol:
        res += i[0]
    return res

def sumar_pesos(sol):
    res = 0
    for i in sol:
        res += i[1]
    return res

# ------------------------ EJERCICIO 2 ------------------------
"""
El problema de Separación en R Cliques (SRC) se enuncia como: Dado un grafo, y un valor entero R, ¿se pueden
separar todos los vértices del gráfo en a lo sumo R cliques? (cada clique puede tener una cantidad diferente de vértices).
De una manera más formal, se puede enunciar: ¿existen S1, S1, ..., Sk, subconjuntos disjuntos del conjunto de vértices
V tal que S
i Si = V , k ≤ R, y que que cada subgrafo correspondiente a los Si sea un clique (subgrafo completo)?
Demostrar que el problema de Separación en R Cliques es un problema NP-Completo. Para esto, recomendamos
recordar que el problema de coloreo es un problema NP-Completo. También, recomendamos recordar cómo fue que
demostramos en clase que K-Clique es un problema NP-Completo (fue con la ayuda de Independent Set).
"""

def verificador(grafo, solucion, R):
    # O(1)
    if len(solucion) > R: 
        return False 
    
    for s in solucion:
        if no_es_clique(grafo, s):
            return False
    
    return True
    

def no_es_clique(grafo, s):
    for v in s:
        for w in s:
            if v == w: 
                continue
            if not grafo.estan_unidos(v, w):
                return True
    return False


# ------------------------ EJERCICIO 3 ------------------------
"""
Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso. Está viendo cómo se
predice que evolucionará el precio de un inmueble (el cual no poseen, pero pueden comprar). Tiene la información de
estas predicciones en el arreglo p, para todo día i = 1, 2, ..., n. Osvaldo quiere determinar un día j en el cuál comprar la
casa, y un día k en el cual venderla (k > j), suponiendo que eso sucederá sin lugar a dudas. El objetivo, por supuesto,
es la de maximizar la ganancia dada por p[k] - p[j].
Implementar un algoritmo de programación dinámica que permita resolver el problema de Osvaldo. Indicar y
justificar la complejidad del algoritmo implementado.
"""

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

# ------------------------ EJERCICIO 4 ------------------------


# ------------------------ EJERCICIO 5 ------------------------
"""
Resolver el problema de Osvaldo (ejercicio 3) pero por división y conquista. 

Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso. Está viendo cómo se
predice que evolucionará el precio de un inmueble (el cual no poseen, pero pueden comprar). Tiene la información de
estas predicciones en el arreglo p, para todo día i = 1, 2, ..., n. Osvaldo quiere determinar un día j en el cuál comprar la
casa, y un día k en el cual venderla (k > j), suponiendo que eso sucederá sin lugar a dudas. El objetivo, por supuesto,
es la de maximizar la ganancia dada por p[k] - p[j].

Ejemplo: p = [100, 50, 400, 23, 70, 900, 49, 1000, 2000, 10] 
Conviene comprar en el día 4 (23) y vender en el día 9 (2000).

Indicar y justificar adecuadamente la complejidad del algoritmo implementado. 
Es probable que la complejidad de ambas soluciones no quede igual, no te estreses por ello.
"""

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
