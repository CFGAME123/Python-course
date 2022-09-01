"""
    se puede usar en todos los bucles
"""

for i in range(10):
    if i==5:
        continue #continue va a obivar lo que encuentre despues de una parte del bucle (en este caso obvia el numero 5 y pasa al 6)
    print(i)
    if i==7:
        break #sirve para salir del bucle y continua con lo que reste de programa
print("programa finalizado")