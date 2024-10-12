import sys
import os
import time
from main import jugar
from src.auxiliares import *
from src.jugar_n_juegos import jugar_n_juegos
from src.cant_vs_tiempo import mostrar_cantidad_vs_tiempo
from src.cant_vs_puntos import mostrar_cantidad_vs_puntos

CARPETA = 'data'

def ejecutar_graficos():
    listas = []
    tamaños = []
    puntos_sofia = []
    puntos_mateo = []

    carpeta_data = CARPETA
    archivos_txt = [f for f in os.listdir(carpeta_data) if f.endswith('.txt')]

    for archivo in archivos_txt:
        ruta_archivo = os.path.join(carpeta_data, archivo) 
        lista = leer_numeros_desde_txt(archivo)
        listas.append(lista)
        
    listas.sort(key=len)
    for lista in listas:
        tamaños.append(len(lista))

    tiempos = []

    for i in listas:
        inicio = time.perf_counter()
        dp = jugar(i)
        #CAMBIAR ESTO
        suma_sofia = dp[0][-1]
        suma_mateo = sum(i) - suma_sofia
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

ejecutar_graficos()