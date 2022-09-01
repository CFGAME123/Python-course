"""
    otro tipo de lista pero esta no se puede modificar
"""

tupla = (4,"hola",5,6,7) #nada se puede agregar, ni sacar, ni modificar dentro de una tupla

#solo se pueden buscar cosas dentro de la tupla cualquier tipo de cosas siempre y cuando se encuentre dentro de esta

#aunque se puede convertir una tupla a una lista pero aun así no se puede modificar xDDDDDDDDDD
lista = list(tupla)

#y se puede convertir una lista en una tupla
tupla = tuple(lista)

print(tupla)