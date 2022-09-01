"""
    Hacer un programa que simule una agenda de contactos. crear un diccionario donde la clave sea el nombre del usuario y el valor sea el telefono, el programa tendra claves de menú de opciones. 
"""

agenda = {}

while True:
    print("1 Nuevo contacto")
    print("2 Borrar contacto")
    print("3 Ver contactos")
    print("4 salir")
    
    opcion = int(input("Opcion: "))
    
    if opcion == 1:
        nombre = input("Nombre del contacto: ")
        telefono = input("Telefono: ")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("contacto agregado")
        else:
            print("Ya existe ese contacto")
            
    elif opcion == 2:
        nombre = input("Nombre del contacto: ")
        if nombre in agenda:
            del(agenda[nombre])
            print("Contacto eliminado")
        else:
            print("Ese contacto no existe")
            
    elif opcion == 3:
        print("Contactos:")
        for clave,valor in agenda:
            print(f"Nombre: {clave},Telefono: {valor}")
    elif opcion == 4:
        print("Gracias por estar aqui")
        break
    
    else:
        print("Error, no existe esa opcion")