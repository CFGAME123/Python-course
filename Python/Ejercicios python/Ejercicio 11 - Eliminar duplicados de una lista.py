"""
    Escribe un progra que tenga una lista y elimina los elementos que se repiten
    y ver si contenido
"""

lista = [1,2,3,'halo',1,2,3,'halo']
conjunto = set(lista)

#2do metodo
lista=list(set(lista))

print(conjunto)