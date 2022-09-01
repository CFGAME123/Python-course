"""
    Hacer un programa para detectar si una frase introducida por el usuario termina con un punto o no. deberas imprimir por la consola una de las siguientes opciones:
    termina con un punto
    o
    de lo contrario
    no termina con un punto
"""

frase = input("Escribe algo con punto (opcional): ")

if frase.endswith("."):
    print(frase)
    print("Termina en un punto")
else:
    print(frase)
    print("No termina en un punto")