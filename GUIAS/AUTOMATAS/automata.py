class Automata():
    def __init__(self):
        """
        Constructor de la clase.
        """
        pass

    def estado(self, nombre, es_inicial=False, es_final=False):
        """
        Para agregar un nuevo estado. 
        El parámetro es_inicial determina si el nuevo estado es además el estado inicial 
            (si ya había un estado inicial, lanzará una excepción). 
        El parámetro es_final indica si dicho estado es un estado de finalización 
            (False por defecto).
        """
        pass

    def transicion_estado(nombre1, nombre2, simbolo):
        """
        Agrega la transición de estados para el símbolo indicado. 
        El símbolo "" (cadena vacía, epsilón) se considera como un símbolo especial de "branching" inmediato. 
        Considera que si desde un estado ya hay una transición por medio de un símbolo, y se agrega otro más, 
        entonces se harán ambas transiciones (considerar lo analizado para un AFND).
        """
        pass