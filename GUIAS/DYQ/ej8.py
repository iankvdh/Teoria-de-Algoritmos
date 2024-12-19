"""
Dados un conjunto de n elementos, y 2 arreglos de longitud n, con dichos elementos. 
El arreglo A está completamente ordenado de menor a mayor. 
El arreglo B se encuentra desordenado. Indicar, por división y conquista, la cantidad de inversioes necesarias 
al arreglo B para que quede ordenado de menor a mayor, con un orden de complejidad mejor que O(n^2). 
Justificar el orden del algoritmo mediante el teorema maestro.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "en tiempo mejor que O(n^2)". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
"""

def contar_inversiones(A, B):
    return _contar_inversiones(A, B, 0, len(B) - 1)

def _contar_inversiones(A, B, ini, fin):
    if ini == fin:
        return 0
    medio = (ini + fin) // 2
    inv_izq = _contar_inversiones(A, B, ini, medio)
    inv_der = _contar_inversiones(A, B, medio + 1, fin)
    return inv_izq + inv_der + _merge(A, B, ini, medio, fin)

def _merge(A, B, ini, medio, fin):
    i = ini
    j = medio + 1
    inv = 0
    while i <= medio and j <= fin:
        if B[i] > B[j]:
            inv += medio - i + 1
            j += 1
        else:
            i += 1
    return inv

# Resuelvo con teorema maestro...

# T(n) = AT(n/B) + O(n^C)

# A = 2 (llamo 2 veces recursivamente)
# B = 2 (parto el arreglo en 2)
# C = 1 (costo  de partir y juntar es O(n))

# A es natural - B es Real, >1, cte - Caso base es cte

# logB(A) = log2(2) = 1 = C --> T(n) = O(n^C * logB(n)) = O(n log n)