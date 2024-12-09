"""
Implementar un Autómata Finito No Determinista que acepte las cadenas que cumplan con la expresión regular:
(aab)*(a, aba)*

Como recordatorio:

El símbolo * indica que el símbolo anterior (o grupo, si está entre paréntesis) puede aparecer tantas veces 
como sea (puede ser ninguna o muchas) de forma contigua.

Esta expresión acepta todas las cadenas que tengan una cantidad indefinida de aab como inicio, luego puedan 
tener una cantidad indefinida de a o aba (que pueden estar intercaladas).
"""
from automata import Automata

def expresion():
    a = Automata()

    # https://www.cs.odu.edu/~zeil/automat/automat.cgi?saved=1&lang=eyJzcGVjaWZpY2F0aW9uIjoiYXV0b21hdG9uRkEiLCJjcmVhdGVkQnkiOiJBbm9ueW1vdXMiLCJwcm9ibGVtSUQiOiIiLCJ1bmxvY2vGDHN0YXRlcyI6W3sibGFiZWwiOiIwIiwiaW5pdGlhbCI6dHJ1ZSwiZmluyg14Ijo3NywieSI6MTk5fSzKOTHMOWZhbHPTOjIyNsU7MjAxzDsy3zvEOzQ3Mcc7Nsw7M987xDszODPFOzMyMn1dLCJ0cmFuc2nkAUPmAPpmcm9t5wD5dG%2FnAMnIX2EixG3HIsQZxSLkALDJIlxuYswlxBzFJeQAmsglYlxuzUrEHN5sySLMR2EifV19
    
    a.estado('0', es_inicial=True, es_final=True)
    a.estado('1')
    a.estado('2')
    a.estado('3')
    a.estado('4', es_final=True)
    a.estado('5')
    a.estado('6', es_final=True)
    a.estado('7')
    a.estado('8')
    a.estado('9')
    a.estado('10', es_final=True)
    
    a.transicion_estado("0","1","")
    a.transicion_estado("1", "2","a")
    a.transicion_estado("2","3","a")
    a.transicion_estado("3","4","b")
    a.transicion_estado("4","0","")
    a.transicion_estado("4","5","")
    a.transicion_estado("0","5","")
    a.transicion_estado("5","6","a")
    a.transicion_estado("6","5","")
    a.transicion_estado("5","7","")
    a.transicion_estado("7","8","a")
    a.transicion_estado("8","9","b")
    a.transicion_estado("9","10","a")
    a.transicion_estado("10","5","")

    return a