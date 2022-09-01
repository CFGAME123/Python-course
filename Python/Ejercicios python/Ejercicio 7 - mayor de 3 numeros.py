"""
    Hacer un programa que pida 3 numeros y determine cual es el mayor
"""

numero1 = int(input("Escribe un numero: "))
numero2 = int(input("Escribe un numero: "))
numero3 = int(input("Escribe un numero: "))

if numero1 >= numero2 and numero1 >= numero3:
    print("numero 1 es el mayor")
elif numero2 >= numero1 and numero2 >= numero3:
    print("numero 2 es el mayor")
elif numero3 >= numero2 and numero3 >= numero1:
    print("numero 3 es el mayor")