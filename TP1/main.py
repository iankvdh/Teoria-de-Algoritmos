import os
import sys
from src.auxiliares import leer_numeros_desde_txt

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

def cargar_set_datos(ruta_archivo_abs):
    try:
        if os.path.isabs(ruta_archivo_abs):
            lista = leer_numeros_desde_txt(ruta_archivo_abs)
            resultado, suma_s, suma_m = jugar(lista)
            print("\n".join(resultado))
            print("--------------------")
            print(f"Total de Sophia: {suma_s}")
            print(f"Total de Mateo: {suma_m}")
        else:
            print("La ruta no es absoluta.")
    except Exception as e:
        print("Error al cargar el archivo: ", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Ejecute de la siguiente manera: python main.py <ruta_absoluta_set_datos>")
        sys.exit(1)

    ruta_abs = sys.argv[1]
    cargar_set_datos(ruta_abs)