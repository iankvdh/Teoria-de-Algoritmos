"""
Modificar el algoritmo anterior para que, dada una lista de enteros positivos L y un entero n, 
devuelva un subconjunto de L que sume exactamente n, o, en caso de no existir, 
que devuelva el subconjunto de suma máxima sin superar el valor de n.
"""

def subconjuntos_que_suman_n(L, n):
    res = []
    _subconjuntos_que_suman_n(L, n, 0, [], res)
    if len(res) == 0:
        aux = []
        for num in L:
            if num < n:
                aux.append(num)
        res.append(aux)
        return res
    return res

def _subconjuntos_que_suman_n(L, n, i, sol_parcial, res):
    if sum(sol_parcial) == n:
        res.append(sol_parcial[:])
        return

    if i == len(L) or sum(sol_parcial) > n:
        return

    sol_parcial.append(L[i])
    _subconjuntos_que_suman_n(L, n, i+1, sol_parcial, res)
    sol_parcial.pop()

    _subconjuntos_que_suman_n(L, n, i+1, sol_parcial, res)