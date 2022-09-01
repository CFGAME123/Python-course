"""
    Hacer un programa que pida una cadena por teclado y luego que meta los caracteres en una lista sin repetir caracteres
"""

cadena = input("Escribe algo: ")
lista = []
for i in cadena:
    if i not in lista:
        lista.append(i)
print(f"lista: \n{lista}")