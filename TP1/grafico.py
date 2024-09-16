import sys
import time
from implementacion_optima import jugar
from src.auxiliares import *
from src.jugar_n_juegos import jugar_n_juegos
from src.cant_vs_tiempo import mostrar_cantidad_vs_tiempo
from src.cant_vs_puntos import mostrar_cantidad_vs_puntos

def main():
    listas = []
    tamaños = []
    puntos_sofia = []
    puntos_mateo = []

    for i in ["20.txt","25.txt","50.txt","100.txt","1000.txt","5000.txt","10000.txt","15000.txt","20000.txt", "25000.txt", "30000.txt"]:
        lista = leer_numeros_desde_txt(i)
        listas.append(lista)
        tamaños.append(len(lista))

    tiempos = []

    for i in listas:
        inicio = time.perf_counter()
        _, suma_sofia, suma_mateo = jugar(i)
        puntos_sofia.append(suma_sofia)
        puntos_mateo.append(suma_mateo)
        fin = time.perf_counter()
        tiempos.append( (fin - inicio) * 1000) # milisegundos

    if len(sys.argv) > 1:
        grafico = sys.argv[2]
        if grafico == "tiempo_vs_cantidad":
            mostrar_cantidad_vs_tiempo(tamaños, tiempos)
        elif grafico == "puntos_vs_cantidad":
            mostrar_cantidad_vs_puntos(tamaños, puntos_sofia, puntos_mateo)
        elif grafico == "victorias_sofia":
            if len(sys.argv) > 3:
                n = int(sys.argv[4])
                jugar_n_juegos(n)
            else:
                jugar_n_juegos()
        else:
            print("Opción no válida.")
    else:
        print("Por favor, ejecute directamente el archivo {ejecutar_graficos.sh}.")

main()