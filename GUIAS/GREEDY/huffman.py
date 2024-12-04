"""
Huffman plantea una forma de comprimir un texto en base a la frecuencia de los caracteres en el mismo.

1. Contar frecuencias de caracteres
2. Crear hojas para todos los elementos
3. Armar un heap de MINIMOS (en el nivel más bajo)
4. Sacar 2 elementos, unirlos y meterlos de nuevo en el heap
5. Repetir paso 4, hasta llegar a la raiz.
6. "Nombrar"/"Pesar" aristas del arbol: IZQ = 0, DER = 1
7. Recorrer las frecuencias y reconstruir el texto con el arbol.
"""

def huffman(texto):
    frecuencias = calcular_frecuencias(texto)
    q = Heap()
    for caracter in frecuencias:
        frecuencia = frecuencias[caracter]
        q.encolar(Hoja(caracter, frecuencia))
    
    while q.cantidad() > 1:
        t1 = q.desencolar()
        t2 = q.desencolar()
        q.encolar( Arbol(t1, t2, t1.frecuencia + t2.frecuencia))
    
    return codificar(q.desencolar())

# auxiliares
def codificar(caracter):
    pass
def Heap():
    pass
def Hoja():
    pass
def Arbol():
    pass
def calcular_frecuencias(texto):
    pass

# Palabras para seguimiento: MAUASAKATAI, ORNITORRINCO, RECURSARNOESOPCION