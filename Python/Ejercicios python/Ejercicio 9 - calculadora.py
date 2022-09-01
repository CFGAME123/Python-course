"""
    Construir un programa que simule el funcionamiento de una calculadora que puede realizar las 4 operaciones aritmeticas basicas (suma, resta, multiplicacion, divicion). el usuario debe especificar la operacion con el primer caracter del nombre de la operacion.
"""

suma = "s" 
resta = "r"
multiplicacion = "m"
divicion = "d"

print(" \n suma: {} \n resta: {} \n multiplicacion: {} \n divicion: {} \n".format(suma, resta, multiplicacion, divicion))

seleccion = input("seleciona una operacion: ").lower()

if seleccion == 's':
    print("has seleccionado la suma")
    
    num1 = float(input("escribe un numero: "))
    num2 = float(input("escribe un numero: "))
    resultado = num1+num2
    
    print("el resultado es: {}".format(resultado))
    
elif seleccion == 'r':
    print("has seleccionado la resta")
    
    num1 = float(input("escribe un numero: "))
    num2 = float(input("escribe un numero: "))
    resultado = num1-num2
    
    print("el resultado es: {}".format(resultado))
    
elif seleccion == 'm':
    print("has seleccionado la multiplicacion")
    
    num1 = float(input("escribe un numero: "))
    num2 = float(input("escribe un numero: "))
    resultado = num1*num2
    
    print("el resultado es: {}".format(resultado))
    
elif seleccion == 'd':
    print("has seleccionado la divicion")
    
    num1 = float(input("escribe un numero: "))
    num2 = float(input("escribe un numero: "))
    resultado = num1/num2
    
    print("el resultado es: {}".format(resultado))

else:
    print("Selecciona una operacion disponible")