# ------------------------ EJERCICIO 1 ------------------------

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
        else:
            return sol_optima[:] # O(n)

    # chequeo si la parcial es compatible (no se pasa de k, ni de W)
    sol_parcial.append(elementos[indice])
    if es_compatible(sol_parcial, W, k):
        sol_optima = _k_mochila_min(elementos, W, k, indice + 1, sol_optima, sol_parcial)

    sol_parcial.pop()
    return _k_mochila_min(elementos, W, k, indice + 1, sol_optima, sol_parcial)


def es_compatible(sol, W, k):
    print(sol)
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
