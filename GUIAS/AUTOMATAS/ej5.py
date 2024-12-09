"""
Implementar un Autómata Finito No Determinista que acepte las cadenas que cumplan con la expresión regular:
((ab)+ba*)?(b*(ab)*)

Notar que la expresión es equivalente a:
((ab)+ba*)?b*(ab)*

Como recordatorio:

El símbolo + indica que el símbolo anterior (o grupo, si está entre paréntesis) aparece al menos una vez (puede aparecer muchas veces, de forma contigua).
El símbolo ? indica que el símbolo anterior (o grupo, si está entre paréntesis) puede aparecer una vez, o no estar (es decir, es opcional).
El símbolo * indica que el símbolo anterior (o grupo, si está entre paréntesis) puede aparecer tantas veces como sea (puede ser ninguna o muchas) de forma contigua.
"""
from automata import Automata

def expresion():
    a = Automata()

    a.estado('A', es_inicial=True, es_final=True)
    a.estado('B')
    a.estado('C', es_final=True)
    a.estado('D', es_final=True)
    a.estado('E')
    a.estado('F')
    a.estado('I', es_final=True)
    a.estado('G', es_final=True)
    a.estado('J', es_final=True)
    a.estado('K', es_final=True)
    a.estado('H', es_final=True)

    a.transicion_estado('A', 'C', 'b')
    a.transicion_estado('C', 'E', 'a')
    a.transicion_estado('E', 'H', 'b')
    a.transicion_estado('C', 'C', 'b')
    a.transicion_estado('A', 'B', 'a')
    a.transicion_estado('B', 'D', 'b')
    a.transicion_estado('D', 'G', 'b')
    a.transicion_estado('G', 'C', 'b')
    a.transicion_estado('D', 'F', 'a')
    a.transicion_estado('F', 'I', 'b')
    a.transicion_estado('I', 'F', 'a')
    a.transicion_estado('I', 'G', 'b')
    a.transicion_estado('G', 'J', 'a')
    a.transicion_estado('J', 'J', 'a')
    a.transicion_estado('J', 'K', 'b')
    a.transicion_estado('K', 'C', 'b')
    a.transicion_estado('K', 'E', 'a')
    a.transicion_estado('H', 'E', 'a')   

    return a