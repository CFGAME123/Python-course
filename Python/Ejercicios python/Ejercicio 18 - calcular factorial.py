"""
    Hacer un programa para calcular el factorial de un numero positivo
"""

numero = int(input("Escribe un numero: "))
while numero <0:
    print("Tiene que ser positivo")
    numero = int(input("Escribe un numero: "))
    
#calcular factorial
factorial = 1
for i in range(1,numero+1):
    factorial *= i
print("resultado: {}".format(factorial))