import random as rd

class Grafo:
    # Grafo: estructura de datos que representa un conjunto de vertices y aristas
    def __init__(self , dirigido = False):
        self.vertices = {}
        self.dirigido = dirigido

    # añade un vertice al grafo
    def agregar_vertice(self, vertice):
        self.vertices[vertice] = {}

    # añade una arista al grafo
    def agregar_arista(self, origen, destino, peso=1):
        self.vertices[origen][destino] = peso
        if not self.dirigido:
            self.vertices[destino][origen] = peso

    # obtiene todos los vertices del grafo
    def obtener_vertices(self):
        return self.vertices.keys()
    
    # obtiene todas las aristas del grafo
    def obtener_aristas(self):
        aristas = []
        for vertice in self.vertices:
            for adyacente in self.vertices[vertice]:
                aristas.append((vertice, adyacente, self.obtener_peso(vertice, adyacente)))
        return aristas

    # obtiene los adyacentes de un vertice en el grafo
    def adyacentes(self, vertice):
        return self.vertices[vertice].keys()
    
    # obtiene el peso de una arista
    def obtener_peso(self, origen, destino):
        return self.vertices[origen][destino]

    # obtiene un vertice aleatorio del grafo
    def obtener_vertice_aleatorio(self):
        return rd.choice(list(self.vertices.keys()))

    # retorna si un vertice esta en el grafo o no
    def contiene_arista(self, origen, destino):
        return destino in self.vertices[origen]
    
    # retorna si un vertice esta en el grafo o no
    def contiene_vertice(self, vertice):
        return vertice in self.vertices
    
    # retorna la cantidad de vertices del grafo
    def cantidad_vertices(self):
        return len(self.vertices)
    
    # retorna la cantidad de aristas del grafo
    def cantidad_aristas(self):
        return sum([len(self.vertices[vertice]) for vertice in self.vertices])
    
    # elimina arista del grafo
    def eliminar_arista(self, origen, destino):
        del self.vertices[origen][destino]
        if not self.dirigido:
            del self.vertices[destino][origen]
    
    # elimina vertice del grafo
    def eliminar_vertice(self, vertice):
        for v in self.vertices:
            if vertice in self.vertices[v]:
                del self.vertices[v][vertice]
        del self.vertices[vertice]
    
    # modifica el peso de una arista
    def modificar_peso(self, origen, destino, peso):
        self.vertices[origen][destino] = peso
        if not self.dirigido:
            self.vertices[destino][origen] = peso
