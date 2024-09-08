def turno_s(lista, inicio, fin):
    return inicio if lista[inicio] >= lista[fin] else fin

def turno_m(lista, inicio, fin):
    return fin if lista[inicio] >= lista[fin] else inicio

def jugar(lista):
    turno = "s"
    suma_s = 0
    suma_m = 0
    inicio = 0
    res = []
    fin = len(lista)-1
    while fin >= inicio:
        if turno == "s":
            saco = turno_s(lista, inicio, fin)
            suma_s += lista[saco]
            if saco == inicio:
                res.append("Primera moneda para Sophia")
                inicio += 1
            else:
                res.append("Última moneda para Sophia")
                fin -= 1
            turno = "m"
        else:
            saco = turno_m(lista, inicio, fin)
            suma_m += lista[saco]
            if saco == inicio:
                res.append("Primera moneda para Mateo")            
                inicio += 1
            else:
                res.append("Última moneda para Mateo")                
                fin -= 1
            turno = "s"
    return res, suma_s, suma_m