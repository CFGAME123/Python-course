"""
    Crear un programa que tenga una lista, cada cliente tiene su nombre, apellido y DNI
"""
def agregar(nombre,apellido,Tarjeta):
    cliente = {}
    cliente = ["Nombre"] = nombre
    cliente = ["Apellido"] = apellido
    cliente = ["T.I"] = tarjeta
    
    clientes.append(cliente)
    
def mostrar_clientes(clientes):
    for i in clientes:
        print(f"Nombre: {i['nombre']},Apellido:{i[apellido]},T.I:{[tarjeta]}")
    
def mostrar_cliente(clientes,tarjeta):
    for i in clientes:
        if i['tarjeta'] == tarjeta:
            print(f"Nombre: {i['nombre']},Apellido:{i[apellido]},T.I:{[tarjeta]}")
            return True
    return False

def eliminar_cliente(cliente,tarjeta):
        for i in clientes:
            if i['tarjeta'] == tarjeta:
                clientes.remove(i)
                return True:
        return False
    
clientes = []

while True:
    print("""\t Menú
1 agregar
2 Mostrar clientes
3 Clientes por T.I
4 Eliminar clientes
5 Salir """)
    
opcion = int(input("Digite una opcion: "))
print()
if opcion == 1:
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    Tarjeta = input("T.I: ")
elif opcion == 2:
    mostrar_clientes(clientes)
elif opcion == 3:
    Tarjeta = input("Escribe la tarjeta: ")
    if mostrar_cliente(clientes,tarjeta):
        print("Cliente encontrado")
    else:
        print("Cliente no encontrado")
elif opcion == 4:
    Tarjeta = input("Escribe la tarjeta: ")
    if eliminar_cliente(clientes,tarjeta):
        print("Cliente eliminado")
    else:
        print("Cliente no encontrado")
elif opcion == 5
    break
else:
    print("Error")
