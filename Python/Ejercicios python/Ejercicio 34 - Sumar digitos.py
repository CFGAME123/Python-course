"""
    Desarrollar un programa que permita
    sumar los digitos de un numero con ayuda de una funcion recursiva
"""

def sumar_digitos(num):
    if num == 0:
        resultado = 0
    else:
        resultado = sumar_digitos(num/10) + (num%10)
        
    return resultado

valor = sumar_digitos(123)
print(valor)
