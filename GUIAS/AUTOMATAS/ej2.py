"""
Implementar un Autómata Finito Determinista que describa al Lenguaje que acepta todos las cadenas de 0 y 1s tales que tienen una cantidad par tanto de 0s como de 1s.
"""
from automata import Automata

def automata_pares_1y0():
    a = Automata()

    a.estado("q00", es_inicial=True, es_final=True)
    a.estado("q01")
    a.estado("q10")
    a.estado("q11")

    a.transicion_estado("q00", "q10", "0")
    a.transicion_estado("q00", "q01", "1")
    a.transicion_estado("q01", "q11", "0")
    a.transicion_estado("q01", "q00", "1")
    a.transicion_estado("q10", "q00", "0")
    a.transicion_estado("q10", "q11", "1")
    a.transicion_estado("q11", "q01", "0")
    a.transicion_estado("q11", "q10", "1")

    return a