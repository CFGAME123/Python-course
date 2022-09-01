"""
    bloque de codigo que estaran dentro del nuestro programa que nos 
    ayudaran a resolver un problema especifico dentro del programa y nos ayudara a reutilizar codigo
    
    existen 2 funciones
    con retorno
    sin retorno
"""
#funcion sin retorno de valor

def saludo():
    print("InquisiGOD")
saludo() #llamar la funcion nos ayudara a ejecutar lo que tengamos dentro del cuerpo de la funcion 

def funcion_parametros(saludos): #funcion con parametros
    print("hola".format(saludos))
funcion_parametros("Jorge - 052")

def tabla(num):
    for i in range(1,11):
        print(f"{num}*{i} = {num*i}")
tabla(20)
print("\n")
tabla(30)