# Implementar, por división y conquista, una función que dado un arreglo sin elementos repetidos 
# y casi ordenado (todos los elementos se encuentran ordenados, salvo uno), obtenga el elemento fuera de lugar. 
# Indicar y justificar su complejidad temporal.

def elemento_desordenado(arr):
    return arr[elemento_desordenado_wrapper(arr, 0, len(arr) - 1)]

def elemento_desordenado_wrapper(arr, inicio, fin):
    if inicio == fin:
        return 0
    
    mitad = (inicio + fin) // 2

    if arr[mitad - 1] < arr[mitad] and arr[mitad] > arr[mitad + 1]:
        return mitad

    return elemento_desordenado_wrapper(arr, inicio, mitad) + elemento_desordenado_wrapper(arr, mitad + 1, fin)

# Resuelvo con teorema maestro...

# T(n) = AT(n/B) + O(n^C)

# A = 2 (llamo 2 veces recursivamente)
# B = 2 (parto el arreglo en 2)
# C = 0 (costo  de partir y juntar es O(1))

# A es natural - B es Real, >1, cte - Caso base es cte

# logB(A) = log2(2) = 1 > C --> T(n) = O(n^logB(A)) = O(n)
