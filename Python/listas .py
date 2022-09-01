"""
    aca podemos guaqrdar todo tipo de cosas, y se crean con corchetes y se su contenido se separa con comas "," 
"""

lista = ['lunes', 'martes','miercoles','jueves','viernes',['sabado','domingo']] #lista y so contenido
lista2 = [1,2,3]
lista3 = [True,False]
lista4 = [10.9,20.3]

print(lista) #para ver su contenido se puede llamar toda la variable pero si deseas ver algo concreto puedes seleccionarlo, su contenido empieza desde el indice 0 (lunes) hasta el final (4 - viernes). tambien se podria empezar con numeros negtivos es decir empieza desde el final hasta el principio. Tambien se puede seleccionar el contenido que deseamos ver usando print(lista[0:???]) 

print(len(lista2)) #len nos ayudara a saber la cantidad de elementos dentro de una lista

lista5 = ['hola','saludos']

lista5.uppend(":D") #va a agregar un elemento al final de la lista de cualquier tipo dentro de los ()
lista5.insert(2,":3") #nos ayuda a insertar elementos ubicandolos en donde que queremos y el elemento que deseamos
lista5.extend([6,7,8]) #nos va a ayudar a insertar todo tipo de elementos al final de la lista de un golpe

lista3 = lista2+lista5 #unir listas

print('hola' in lista5) #buscar un elemento que deseamos usando "in"
print(lista.index('saludos')) #buscar la ubicacion o indice de un elemento en una lista

print(lista.count("hola")) #nos ayuda a saber cuantas veces se repite un elemento dentro de una lista

lista5.pop() #nos ayudada a eliminar al ultimo elemento de la lista, aunque se puede poner exactamente que elemento deseamos eliminar.

lista5.remove() #nos ayuda a borrar algun elemento solo con escribir su nombre
lista5.clear() #nos ayuda a borrar todos los elementos dentro de una lista

lista5.reverse() #que el contenido de la lista el principio al final y el final al principio
lista.sort() #nos ayudara a organizar los elementos ascendentemente y desedentemente seria: lista.sort(reverse=True)