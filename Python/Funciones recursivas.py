#Funciones recursivas | una funcion que se llama a si misma
def cuenta_regresiva(num):
    if num>0:
        print(num)
        cuenta_regresiva(num - 1)
    else:
        print("Boom!!!")
cuenta_regresiva(5)
