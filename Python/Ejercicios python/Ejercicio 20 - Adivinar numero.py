"""
    realizar un Juego para adivinar un numero. para ello generar
    un numero aleatorio entre 0 a 10 y luego ir pidiendo numeros indicando "es mayor" o es "menor" segun sea mayor o menor con respecto a N. el proceso termina cuando el usuario acierta y mostrar el numero de intentos
"""

import random
aleatorio = random.randint(0,10) #numeros que escojera de manera random
contador = 0
while True:
    numero = int(input("Numero: "))
    contador += 1
    if numero>aleatorio:
        print("Mal es menor")
    elif numero<aleatorio:
        print("Mal es mayor")
    else:
        print("Bien adivinaste")
        break

print("Intentos: {}".format(contador))