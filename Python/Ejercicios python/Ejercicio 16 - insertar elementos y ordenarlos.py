"""
    pide numeros y metelos en una lista, cuando usuario meta el numero 0 ya dejaremos de insertar. pr ultimo mostramos los elementos ordenados de menor a mayor
"""

lista = []
salir = False
while not salir:
    numero = int(input("digita un numero: "))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() #nos ayudara a ordenar todo de menor a mayor usando sort()
print("lista ordenada: {} ".format(lista))