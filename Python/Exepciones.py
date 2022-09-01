while True:
    try: #intentar algo | ejemplo de error
        numero = int(input("Digite un numero: " ))
        print(numero + 10)
    except:
        print("ha ocurrido un error")
    else:
        print("programa finalizado correctamente") #metodo mas correcto | agregar un else
        break
    finally:
        print("iteracion finalizada") #se ejecuta independientemente en el bucle tanto con error o sin error

#Continuar el programa
#si todo sale bien ps bien
#si algo malo ocurre
#muestra el mensaje de error
