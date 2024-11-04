"""
Escribir un algoritmo que, utilizando backtracking, dada una lista de enteros positivos L 
y un entero n devuelva todos los subconjuntos de L que suman exactamente n.
"""
def subconjuntos_que_suman_n(L, n):
    res = []
    _subconjuntos_que_suman_n(L, n, 0, [], res)
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

# TESTS

L = [1, 2, 3, 4, 5]
n = 5
print(subconjuntos_que_suman_n(L, n)) # [[1, 4], [2, 3], [5]]

L = [1, 2, 6]
n = 5
print(subconjuntos_que_suman_n(L, n)) # []
