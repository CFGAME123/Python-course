"""
    Es un trozo de codigo que se va a repetir un numero determinado e indeterminado de veces.
    el bucle while se le conoce por es un bucle con un numero de ejecucion indeterminado de veces donde se le pone una condicion para que se pueda ejecutar
"""

import math

numero = int(input("Escribe un numero: "))

while numero<0: #condicion del bucle while
    print("error") #error en caso de que hayas escrito algo mal
    numero = int(input("escribe un numero: ")) #te lo va a volver a pedir

print("su raiz cuadrada es: {} ".format(math.sqrt(numero))) #operacion

#mientras la codicion se siga cumpliendose el programa seguira ejecutandose pero si se incumple; el programa dejara de ejecutarse

#ejercicio 2
i = 0
while i<10: #mostrar el mensaje inferior 10 veces
    print("hola mundo") #mensaje que se mostrara la cantidad de veces requeridas
    i += 1;