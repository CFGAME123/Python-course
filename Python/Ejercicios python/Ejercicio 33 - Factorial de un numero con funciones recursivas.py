"""
Factorial de un numero con recursividad
"""
def factorial(num):
    if num>0:
        resultado = num * factorial(num-1)
    else:
        resultado = 1
    return resultado

valor = factorial(5)
print(valor)
