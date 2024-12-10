"""
El club de Amigos de Siempre prepara una cena en sus instalaciones en la que desea invitar a la máxima 
cantidad de sus n socios. Sin embargo por protocolo cada persona invitada debe cumplir un requisito: 
Sólo puede ser invitada si conoce a al menos otras 4 personas invitadas. 
Dada un lista de tuplas (duplas) de personas que se conocen, nos solicitan seleccionar el mayor 
número posible de invitados. Proponer una estrategia greedy óptima para resolver el problema.
"""

"""
La estrategia greedy sería seleccionar iterativamente las personas que cumplen el requisito de conocer 
al menos a otras 4 personas invitadas y eliminar de la lista a las que no lo cumplen, reduciendo así el 
problema hasta que no haya más candidatos válidos.
"""
from auxiliares import Grafo

# conocidos: lista de pares de personas que se conocen, cada elemento es un (a,b)
def obtener_invitados(conocidos):
    grafo = Grafo()

    for a, b in conocidos:
        if a not in grafo.obtener_vertices():
            grafo.agregar_vertice(a)
        if b not in grafo.obtener_vertices():
            grafo.agregar_vertice(b)
        grafo.agregar_arista(a, b)

    # Aplicar el proceso de eliminación de nodos con grado < 4
    cambios = True
    while cambios:
        cambios = False
        nodos_a_eliminar = [v for v in grafo.obtener_vertices() if len(grafo.adyacentes(v)) < 4]
        
        if nodos_a_eliminar:
            cambios = True
            for nodo in nodos_a_eliminar:
                grafo.borrar_vertice(nodo)

    return grafo.obtener_vertices()
