# Implementar Merge Sort. Justificar el orden del algoritmo mediante el teorema maestro.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    medio = len(arr) // 2
    izq = merge_sort(arr[:medio])
    der = merge_sort(arr[medio:])
    return intercalar_ordenado(izq, der)

def intercalar_ordenado(izq, der):
    i = 0
    j = 0
    res = []
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            res.append(izq[i])
            i += 1
        else:
            res.append(der[j])
            j += 1
    res.extend(izq[i:])
    res.extend(der[j:])
    return res

# Resuelvo con teorema maestro...

# T(n) = AT(n/B) + O(n^C)

# A = 2 (llamo 2 veces recursivamente)
# B = 2 (parto el arreglo en 2)
# C = 1 (costo  de partir y juntar es O(n))

# A es natural - B es Real, >1, cte - Caso base es cte

# logB(A) = log2(2) = 1 = C --> T(n) = O(n^C * logB(n)) = O(n log n)