"""
    Realizar un programa en donde el usuario digite una palabra palindroma
    y determinar si es o no lo es
"""

frase = input("Escribe una frase: ")

#1ro quitamos lo espacios en blanco de la cadena
cadena = cadena.replace(" "," ")

#invertimos la cadena
cadena2 = cadena[::-1]

if cadena == cadena2:
    print("la cadena es un palindromo")
else:
    print("No es palindromo")