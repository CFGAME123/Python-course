"""
    Escriba un programa que tenga dos listas y que, acontinuacion, cree las siguientes listas (de  las que no deben haber repeticiones)
    
    lista de elementos que aparece ne las 2 filas
    lista de elementos que apareceran en la primera lista pero no en la 2da
    lista de elementos que apareceran en la 2da pero no en la primera
    lista de elementos que aparecen en ambas listas
    
"""

lista = [1,2,3,1,2,3]
lista2 = [2,3,4,5,6,7,5,6]

#eliminar repeticiones
a = set(lista)
b = set(lista2)

union = list(a | b)
soloA = list(a-b)
soloB = list(b-a)
Interseccion = list(a&b)

print("{}".format(union))
print("{}".format(soloA))
print("{}".format(soloB))
print("{}".format(Interseccion))