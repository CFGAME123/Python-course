#Lanzar nuestras propias excepciones
def verificando_edad(edad):
    if edad <0:
        raise ValueError("Edad no puede ser negativa") #crear nuestra propia excepcion
    elif edad<18:
        print("Eres muy joven")
    elif edad <20:
        print("Bien, muy bien")
edad = int(input("Escribe tu edad: "))
try:
    verificando_edad(edad)
except ValueError as edadNegativa:
    print(edadNegativa)
