"""
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. 
Además, cada charla tiene asociado un valor de ganancia. Implementar un algoritmo que, 
utilizando programación dinámica, reciba un arreglo que en cada posición tenga una charla 
representada por una tripla de inicio, fin y valor de cada charla, e indique cuáles son las 
charlas a dar para maximizar la ganancia total obtenida. 
Indicar y justificar la complejidad del algoritmo implementado.
"""

# ordenar charlas por horario de fin
# para cada charla, buscar la charla que no se solape con ella
# calcular el valor de la charla actual + el valor de la charla que no se solapa
# tomar el máximo entre el valor calculado y el valor de la charla anterior

# OPT(i) = max(valor(i) + OPT(p(i)), OPT(i-1))


def buscar_charlita_que_no_solape(charlas,ini,fin,i):
    if ini == fin:
        return ini
    mitad = (ini + fin) // 2
    if charlas[i][0] > charlas[mitad][1]:
        return buscar_charlita_que_no_solape(charlas,mitad+1,fin,i)
    return buscar_charlita_que_no_solape(charlas,ini,mitad,i)


def scheduling(charlas):
    p = [None] * (len(charlas) + 1) 
    opt = [None] * (len(charlas) + 1)
    p[0] = 0
    opt[0] = 0
    charlas = sorted(charlas, key=lambda x: x[1])
    print(charlas)

    for i in range(1,len(charlas) + 1):
        ini = charlas[i-1][0]
        fin = charlas[i-1][1]
        valor = charlas[i-1][2]
        p[i] = buscar_charlita_que_no_solape(charlas,0, len(charlas)-1, i-1)
    
    print(f'ARREGLO P: {p}')

    for i in range(1,len(charlas)+1):
        valor = charlas[i-1][2]
        opt[i] = max(valor + opt[p[i]], opt[i-1])

    print(f'ARREGLO OPT: {opt}')

    sol = reconstruir_charlas(charlas, opt, p)
    return sol


def reconstruir_charlas(charlas, opt, p):
    sol = []
    i = len(opt)-1
    
    while i > 0:
        if (opt[i-1]) < (charlas[i-1][2] + opt[p[i]]):
            sol.append(charlas[i-1])
            i = p[i]
            continue
        i-=1

    sol.reverse()
    return sol

# test
charlas = [
    (0, 4, 2),   # (horario_inicio, horario_fin, valor)
    (1, 6, 4),
    (5, 8, 4),
    (2, 11, 7),
    (9, 12, 2),
    (10, 13, 1)
]

print(scheduling(charlas))

"""
def sche_dinamico(n, p, valor):
   if n == 0:
       return 0
   M_SCHE = [0] * (n + 1)
   M_SCHE[0] = 0
   for j in range(1, n + 1):
       M_SCHE[j] = max(valor[j] + M_SCHE[p[j]], M_SCHE[j-1])
   return M_SCHE[n]
"""

# Complejidad: O(n*log(n)) donde n es la cantidad de charlas que se tienen.