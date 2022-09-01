def dividir():
    while True:
        try:
            num1  = int(input("escribe un numero: "))
            num2 = int(input("escribe un numero: "))
            resultado = num1+num2
            print("resultado".format(resultado))
        except ValueError:
            print("Digita bien los numeros")
        except ZeroDivisionError:
            print("No se divide entre 0")
        else:
            break

dividir()
