import sys
import os
import time
from main import jugar
from main import reconstruir_monedas_tomadas_por_sophia
from src.auxiliares import *
from src.jugar_n_juegos import jugar_n_juegos
from src.cant_vs_tiempo import mostrar_cantidad_vs_tiempo
from src.cant_vs_puntos import mostrar_cantidad_vs_puntos
from src.variabilidad import mostrar_tiempo_vs_variabilidad
from src.reconstruccion_vs_tiempo import reconstruccion_vs_tiempo

CARPETA = 'data'

def monedas_desde_archivos():
    """
    Lee los archivos de la carpeta data y devuelve una lista con los tamaños
    de las listas de monedas y otra lista con las listas de monedas.
    """
    listas = []
    tamaños = []
    carpeta_data = CARPETA
    archivos_txt = [f for f in os.listdir(carpeta_data) if f.endswith('.txt')]

    for archivo in archivos_txt:
        ruta_archivo = os.path.join(carpeta_data, archivo) 
        lista = leer_numeros_desde_txt(archivo)
        listas.append(lista)

    listas.sort(key=len)
    for lista in listas:
        tamaños.append(len(lista))

    return tamaños, listas

def jugar_muchos_arreglos(listas):
    """
    Dada una lista de listas de monedas, devuelve una lista con los tiempos de ejec
    de cada una de las listas. Además, devuelve dos listas con los puntos de Sofia
    y Mateo respectivamente.
    """
    tiempos = []
    puntos_sofia = []
    puntos_mateo = []

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

    return tiempos, puntos_sofia, puntos_mateo

def reconstruir_muchos_arreglos(listas):
    """
    Dada una lista de listas de monedas, devuelve una lista con los tiempos de 
    reconstrucción de cada una de las listas. Además, devuelve dos listas con 
    los puntos de Sofia y Mateo respectivamente.
    """
    tiempos = []
    puntos_sofia = []
    puntos_mateo = []

    for i in listas:
        dp = jugar(i)
        inicio = time.perf_counter()
        reconstruir_monedas_tomadas_por_sophia(i, dp)
        fin = time.perf_counter()
        tiempos.append( (fin - inicio) * 1000) # milisegundos

    return tiempos


def ejecutar_graficos():

    """
    Función que se encarga de ejecutar los gráficos según los argumentos pasados por
    consola. Si no se pasan argumentos, se imprime un mensaje de error.
    """

    if len(sys.argv) > 1:
        grafico = sys.argv[2]
        if grafico == "tiempo_vs_cantidad":
            tamaños, listas = monedas_desde_archivos()
            tiempos, _, _ = jugar_muchos_arreglos(listas)
            mostrar_cantidad_vs_tiempo(tamaños, tiempos)
        elif grafico == "puntos_vs_cantidad":
            tamaños, listas = monedas_desde_archivos()
            _, puntos_sofia, puntos_mateo = jugar_muchos_arreglos(listas)
            mostrar_cantidad_vs_puntos(tamaños, puntos_sofia, puntos_mateo)
        elif grafico == "victorias_sofia":
            if len(sys.argv) > 3:
                n = int(sys.argv[4])
                jugar_n_juegos(n)
            else:
                jugar_n_juegos()
        elif grafico == "tiempo_vs_variabilidad":
            mostrar_tiempo_vs_variabilidad()
        elif grafico == "reconstruccion_vs_tiempo":
            tamaños, listas = monedas_desde_archivos()
            tiempos = reconstruir_muchos_arreglos(listas)
            reconstruccion_vs_tiempo(tamaños, tiempos)
        else:
            print("Opción no válida.")

    else:
        print("Por favor, ejecute directamente el archivo {ejecutar_graficos.sh}.")

ejecutar_graficos()