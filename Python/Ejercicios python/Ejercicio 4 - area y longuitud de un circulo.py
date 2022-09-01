"""
    Hacer un programa para ingresar el radio de un circulo y se reporte su area y la longuitud de la circunferencia
"""

import math #importar modulos :O
radio = float(input("escribe el radio: "))

area= math.pi * radio**2  #llamar el valor de pi que está dentro del modulo importado
longuitud = 2 * math.pi * radio

print("el area es: {}".format(area:))
print("la longuitud es: {}".format(longuitud:))