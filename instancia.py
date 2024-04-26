"""Módulo para leer y escribir instancias de PDG.

El grafo se almacena en formato graph6 y sparse6.
Los vectores se almacenan como cadena de caracteres. 
"""

import networkx as nx
import ast

def escribir_lista(lista, ruta):
    with open(ruta, 'w', encoding="utf-8") as ds:
        ds.write(str(lista))

def escribir_instancia(G, k, u, ruta):
    nx.write_graph6(G, ruta + ".graph")
    escribir_lista(k, ruta + ".list.k")
    escribir_lista(u, ruta + ".list.u")

def leer_lista(ruta):
    with open(ruta, 'r', encoding="utf-8") as ds:
        return ast.literal_eval(ds.read())

def leer_instancia(ruta):
    G = nx.read_graph6(ruta + ".graph")
    k = leer_lista(ruta + ".list.k")
    u = leer_lista(ruta + ".list.u")
    return G, k, u

def escribir_diccionario(lista, ruta):
    escribir_lista(lista, ruta)

def leer_diccionario(ruta):
    return leer_lista(ruta)
