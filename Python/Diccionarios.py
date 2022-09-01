"""
    son otro tipo de coleccion, desorganizado y se dividen en clave y valor.
    donde se puede agregar todo tipo de valores
"""

diccionario = {
    'azul':'blue', #elemento de un diccionario
    'green':'verde',
    'aña':'pankeis'
}

print(diccionario['azul']) #para solo ver el valor de una cosa cosa dentro de un diccionario
diccionario['amarillo'] = 'yelow' #agregar un nuevo elemento al diccionario
diccionario['azul'] = 'BLUE' #modificar el valor
del(diccionario['green']) #borrar un valor o una clave


diccionario2 = {
    'jorge2':{'edad':14,'altura':1.69}
}

diccionario3 = {
    'jorge':{'edad':14,'altura':1.69}
}

print(diccionario)
print(diccionario2)
print(diccionario3[jorge])

equipo = {10:"jorge",7:"jorge2",5:"George"}

print(equipo.get(10,"no existe tu jugador de la casta jorge")) #imprimir un mensaje
print(equipo.keys()) #mostrar solo las claves es decir los nombres de los elementos en el diccionario
print(equipo.values()) #mostrar los valores
print(equipo.items()) #ver tanto claves y valores dentro del diccionario
print(len(equipo))
equipo.clear()