"""
    Hacer un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10. por ejemplo, si el numero es el 5 la lista tendra 5,10,15,20,25 etc...
"""
lista = []
numero = int(input("Escribe un numero: "))
for i in range(1,11):
    lista.append(i*numero)
print("Tabla: {}".format(lista))