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

def buscar_charlita_que_no_solape(charlas,ini,fin,i):
    if ini == fin:
        return ini
    mitad = (ini + fin) // 2
    if charlas[mitad][1] <= charlas[i][0]:
        return buscar_charlita_que_no_solape(charlas,mitad+1,fin,i)
    return buscar_charlita_que_no_solape(charlas,ini,mitad,i)

def scheduling(charlas):
    p = [None] * (len(charlas) + 1) 
    opt = [None] * (len(charlas) + 1)
    p[0] = 0
    opt[0] = 0
    charlas = sorted(charlas, key=lambda x: x[1])

    for i in range(1, len(charlas)+1):
        p[i] = buscar_charlita_que_no_solape(charlas,0,i-1,i-1)
        opt[i] = max(charlas[i-1][2] + opt[p[i]], opt[i-1])
    
    return reconstruir_charlas(charlas, opt, p)

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

# Complejidad: O(n*log(n)) donde n es la cantidad de charlas que se tienen.
