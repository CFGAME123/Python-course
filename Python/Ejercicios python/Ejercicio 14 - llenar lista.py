"""
    llenar una lista con los numeros del 1 al 50 y luego mostrar la lista con un bucle for, los elementos deben mostrarse de la siguiente forma
    1-2-3-4-5 | for
"""

#2do metodo
#lista = list(range(1,51))

lista = []
i = 1
while i <= 50:
    lista.append(i)
    i+=1
    
#imprimiendo los elementos de la lista
for i in lista:
    print(i,end="-")