import os

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

def modelo_lineal(x, m, b):
    return m * x + b

def modelo_cuadratico(x, a, b, c):
    return a * x**2 + b * x + c