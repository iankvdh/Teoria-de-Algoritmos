"""
Implementar un Autómata Finito Determinista que describa al Lenguaje que acepta todos las cadenas de 0 y 1s tales que dicho input represente en binario a una potencia de 2.
"""
from automata import Automata

def automata_potencias_2():
    a = Automata()

    a.estado("q0", es_inicial=True)
    a.estado("q1", es_final=True)
    a.estado("q2")

    a.transicion_estado("q0", "q1", "1")
    a.transicion_estado("q0", "q0", "0")
    a.transicion_estado("q1", "q1", "0")
    a.transicion_estado("q1", "q2", "1")
    a.transicion_estado("q2", "q2", "0")
    a.transicion_estado("q2", "q2", "1")

    return a