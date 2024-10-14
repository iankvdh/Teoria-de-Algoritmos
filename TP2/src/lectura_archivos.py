import os

CARPETA = 'data'

def leer_numeros_desde_txt(nombre_archivo):
    """
    Lee un archivo de texto y devuelve una lista con los números que contiene.
    Si el archivo tiene comentarios, los ignora.
    """
    if not os.path.isabs(nombre_archivo):
        nombre_archivo = 'data/' + nombre_archivo

    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        if lineas[0].startswith('#'):
            lineas = lineas[1:]
        contenido = ''.join(lineas).strip() 
        numeros_str = contenido.split(';')  
        numeros = [int(num) for num in numeros_str]  
    return numeros


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

