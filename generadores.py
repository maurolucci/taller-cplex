import networkx as nx
from itertools import combinations
import random

def generar_oruga(patas):
    """Generador de grafo oruga.
    
    Argumentos:
    ----------
    patas : list[int]
        Lista con el nro de vértices que cuelgan de
        cada vértice del camino central.

    Retorno:
    -------
    G : nx.Graph
    """
    n = len(patas) # Nro. de vertices del camino central
    G = nx.path_graph(n) # Grafo camino
    v = n # Identificador del proximo vertice a agregar 
    for i, m in enumerate(patas):
        for j in range(m):
            G.add_edge(i,v)
            v += 1 # Avanzamos el identificador
    return G

def generar_oruga_aleatorio(n,i,f):
    """Generador de grafo oruga aleatorio.
    
    Argumentos:
    ----------
    n : int
        Número de vértices del camino central.
    i : int
        Mínimo número de colgantes por vértice.
    f : int
        Máximo número de colgantes por vértice.

    Retorno:
    -------
    G : nx.Graph

    Suponemos i <= f.
    """
    patas = [random.randint(i,f) for _ in range(n)]
    return generar_oruga(patas)

def generar_kneser(n, r):
    """Generador de grafo de Kneser K(n,r).
    
    Argumentos:
    ----------
    n : int
        Número de elementos del conjunto.
    r : int
        Número de elementos de los subconjuntos.

    Retorno:
    -------
    G : nx.Graph
    """
    G = nx.Graph() # Grafo vacio
    subconj = list(combinations(range(n), r)) # Lista de subconjuntos
    for i, u in enumerate(subconj):
        for j, v in enumerate(subconj):
            if (i < j and # Control para evitar agregar bucles y aristas por duplicado 
                not set(u).intersection(set(v))): # Control de interseccion vacia
                G.add_edge(i,j)
    return G, subconj

def hay_interseccion_1_1(i1,f1,i2,f2):
    return i1 <= f2 and i2 <= f1

def hay_interseccion_1_2(i1,f1,i2,f2):    
    return hay_interseccion_1_1(i1,f1,i2,12) or hay_interseccion_1_1(i1,f1,0,f2)

def hay_interseccion(i1,f1,i2,f2):
    if i1 < f1 and i2 < f2: # Caso tipo 1 y tipo 1
        return hay_interseccion_1_1(i1,f1,i2,f2)
    elif i1 < f1 and i2 > f2: # Caso tipo 1 y tipo 2
        return hay_interseccion_1_2(i1,f1,i2,f2)
    elif i1 > f1 and i2 < f2: # Caso tipo 2 y tipo 1
        return hay_interseccion_1_2(i2,f2,i1,f1)
    else: # Caso tipo 2 y tipo 2
        return True

def generar_arco_circular(arcos):
    """Generador de grafo arco circular.
    
    Argumentos:
    ----------
    arcos : list[tuple[int,int]]
        Lista de arcos de circunferencia.
        Cada arco es una tupla con su inicio y fin.

    Retorno:
    -------
    G : nx.Graph
    """
    G = nx.Graph() # Inicializamos un grafo vacio
    for j1, (i1,f1) in enumerate(arcos):
        for j2, (i2,f2) in enumerate(arcos):
            if (j1 < j2 # Control para evitar agregar bucles y aristas por duplicado 
                and hay_interseccion(i1,f1,i2,f2)): # Los arcos se intersectan
                G.add_edge(j1,j2)
    return G

def generar_arco_circular_aleatorio(n,i,f):
    """Generador de grafo arco circular aleatorio.
    
    Argumentos:
    ----------
    n : int
        Número de vértices.
    i : float
        Mínima duración de un arco.
    f : float
        Máxima duración de un arco.

    Retorno:
    -------
    G : nx.Graph

    Suponemos i < f.
    """
    arcos = []
    for _ in range(n):
        a = random.uniform(0,12)
        b = random.uniform(i,f)
        if a + b < 12: # Intervalo de tipo 1
            arcos.append((a,a+b))
        else: # Intervalo de tipo 2
            arcos.append((a,(a+b)-12))
    return generar_arco_circular(arcos)