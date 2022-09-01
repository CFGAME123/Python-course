"""
    Hacer un programa donde se deberia imprimir por la consola la palabra con mas caracteres  de dos palabras dadas. en el caso de que ambas palabras tengan la misma cantidad de caracteres deberás mostras el mensaje son iguales
"""

frase1 = input("Escribe una frase cualquiera:  ")
frase2 = input("Escribe otra frase cualquiera: ")

if len(frase1) > len(frase2):
    print(f"{frase1} es mas larga")
elif len(frase2) > len(frase1):
    print(f"{frase2} es mas larga")
else:
    print(f"{frase1} y {frase2} son iguales")