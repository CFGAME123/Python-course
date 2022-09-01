"""
    grupos de elementos desordenados pero estos no pueden ser duplicados
"""

conjunto = set() #set() nos ayudara a poder crear un conjunto vacio

conjunto = { 
    1,2,3,"hola"
} 

#no pueden haber otro tipo de colecciones dentro de un cojunto

conjunto.add(5) #agregar un elemento dentro de un conjunto pero se agrega de manera desordenada
conjunto.discard("hola") #eliminar un elemento dentro de un conjunto
conjunto.clear() #borrar todo el contenido de un conjunto


print(conjunto)
print(3 in conjunto) #buscar un elemento dentro de un conjunto utilizando "in" y saber si no está se usa "not in"


a = frozenset({ #volver un conjunto inmutable usando frozenset() es decir no se puede cambiar, ni agregar, ni eliminar ni nada
    1,2,3
})

b = {
    3,4,5
}

c = a|b #unir 2 conjuntos
c = a&b #intercepccion / ver cuantos elementos tienen en comun
c = a-b #diferencia de conjuntos
c = b-a
c = a^b #diferencia asimetrica
c = {
    1,2,3,4,5
}

print(a.issubset(c)) #ver si un conjunto es un subconjunto del otro usando issubset()
print(c.issuperset(a)) #ver un superconjunto uno del otro
print(a.isdisjoint(b)) #disconexco seria cuando no comparten ningun conjunto en comun
print(c)
print(a == b)
print(len(a))
