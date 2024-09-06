def turno_s(lista, inicio, fin):
    return inicio if lista[inicio] >= lista[fin] else fin

def turno_m(lista, inicio, fin):
    return fin if lista[inicio] >= lista[fin] else inicio

def jugar(lista):
    turno = "s"
    suma_s = 0
    #lista_s = []
    suma_m = 0
    #lista_m = []
    inicio = 0
    fin = len(lista)-1
    largo_lista = len(lista)
    while fin >= inicio:
        if turno == "s":
            saco = turno_s(lista, inicio, fin)
            suma_s += lista[saco]
            #lista_s.append(lista[saco])
            if saco == inicio:
                inicio += 1
            else:
                fin -= 1
            turno = "m"
        else:
            a = turno_m(lista, inicio, fin)
            suma_m += lista[a]
            #lista_m.append(lista[a])
            if a == inicio:
                inicio += 1
            else:
                fin -= 1
            turno = "s"
    return suma_s, suma_m