# Implementar una función, que utilice división y conquista, de orden O(nlogn) que 
# dado un arreglo de n números enteros devuelva true o false según si existe algún 
# elemento que aparezca más de la mitad de las veces. Justificar el orden de la solución. 

# Ejemplos:

# [1, 2, 1, 2, 3] -> false
# [1, 1, 2, 3] -> false
# [1, 2, 3, 1, 1, 1] -> true
# [1] -> true

# Aclaración: Este ejercicio puede resolverse, casi trivialmente, ordenando el arreglo con un algoritmo eficiente, 
# o incluso se puede realizar más rápido utilizando una tabla de hash. Para cumplir con la consigna, resolver 
# sin ordenar el arreglo ni con tabla de hash, sino puramente por división y conquista.

def mas_de_la_mitad(arr):
    return arr.count(_mas_de_la_mitad(arr, 0, len(arr)-1)) > len(arr)//2
    
def _mas_de_la_mitad(arr, inicio, fin):
    if inicio == fin:
        return arr[inicio]
    
    mitad = (inicio + fin) // 2
    
    izq = _mas_de_la_mitad(arr, inicio, mitad)
    der = _mas_de_la_mitad(arr, mitad + 1, fin)
    
    if izq == der:
        return izq
    
    contar_izq = sum(1 for i in range(inicio, fin + 1) if arr[i] == izq)
    contar_der = sum(1 for i in range(inicio, fin + 1) if arr[i] == der)
    
    return izq if contar_izq > contar_der else der

# Resuelvo con teorema maestro...

# T(n) = AT(n/B) + O(n^C)

# A = 2 (llamo 2 veces recursivamente)
# B = 2 (parto el arreglo en 2)
# C = 1 (costo  de partir y juntar es O(n))

# A es natural - B es Real, >1, cte - Caso base es cte

# logB(A) = log2(2) = 1 = C --> T(n) = O(n^C * logB(n)) = O(n log n)