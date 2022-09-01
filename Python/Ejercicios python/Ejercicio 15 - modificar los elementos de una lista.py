"""
    llenar una lista con los numeros del 1 al 10, luego modificar los elementos de la lista miltiplicandolos por un valor que el usuario digite
"""

lista = list(range(1,11))
print("\n lista es: ")
for i in lista:
    print(i,end="-")

#multiplicar todos los elementos de la lista
valor = int(input("\n digita un numero: "))
indice = 0
for i in lista:
    lista [indice] *= valor
    indice += 1

#final
print("\n lista final: {}".format(valor))
for i in lista:
    print(i,end="-")