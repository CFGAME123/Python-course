"""
    Desarrollar un programa que pueda calcular el valor del tipo de cambio de moneda (de tu moneda hacia el dolar y viceversa)
"""

def cambio_p_D(peso):
    return pesos/0.00023

def cambio_D_P(dolares):
    return dolares*0.00023

while True:
    print("\n///Opciones///\n")
    print("1 pesos - dolares")
    print("2 dolares - pesos")
    print("3 Salir")
    
opcion = int(input("Opcion: "))

if opcion == 1:
    pesos = float(input("Cantidad de pesos: "))
    print(f"Dolares: {cambio_p_D(pesos): .2f}")
    
elif opcion == 2:
    dolares = float(input("Cantidad de dolares: "))
    print(f"pesos: {cambio_D_P(dolares): .2f}")
    
elif opcion == 3:
    print("Gracias por estar aqui uwu")
    break
    