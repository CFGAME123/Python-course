#Ejemplo del capitulo

"""
edad = int(input("escribe tu edad: "))
if edad >=18:
    print("es mayor de edad")
    
elif edad <= 0:
    print("Escribe una edad real")
    
else:
    print("no es mayor de edad")
"""
    
#condicional anidado 
#sirve para tener diferentes condiciones una dentro de otra
edad = int(input("escribe tu edad: "))
if edad > 0:
    print("edad correcta")
    if edad >=18:
        print("mayor de edad")
else:
    print("edad incorrecta")
    

#condicional combinado
edad = int(input("escribe tu edad: "))
if edad >0 and edad<100: #se puede utilizar cualquier operador logico
    print("edad correcta")
    if edad >=18:
        print("mayor de edad")
else:
    print("edad incorrecta")