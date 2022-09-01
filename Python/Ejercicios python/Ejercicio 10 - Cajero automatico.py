"""
    Hacer un programa que simule un cajero automatico con un saldo incial de 1.000 dolares y tendrá el siguiente menu de opciones
    
    ingresar dinero
    sacar dinero
    mostrar dinero
    salir
    
"""

saldo = 1000

print("|Menú|")
print("Ingresar dinero: 1 ")
print("Retirar dinero : 2 ")
print("Ver saldo:     : 3 ")
print("salir          : 4 ")

opcion = int(input("escribre su seleccion: "))

if opcion == 1:
    extra = float(input("Cuanto dinero desea ingresar?: "))
    saldo += extra
    print("Dinero disponible ahora: {}".format(saldo))
elif opcion == 2:
    retirar = float(input("cuanto desea retirar?: "))
    if retirar > saldo:
        print("no tiene esa cantidad :/ ")
    else:
        print("ahora te queda {} ".format(saldo))

elif opcion == 3:
    print("saldo disponible: {} ".format(saldo))
elif opcion == 4:
    print("gracias por utilizar su cajero automatico")
else:
    print("Error")
