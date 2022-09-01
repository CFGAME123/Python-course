"""
    Hacer un programa que pida la anchura y altura de un rectangulo y con ayuda de una funcion lo dibuje con "*"
"""

def dibujar(ancho,alto):
    for a in range(alto):
        for b in range(ancho):
            print(" * ",end="")
        print("\n")

ancho = int(input("Digita el ancho: "))
alto = int(input("Digita la altura: "))
print("\n")
dibujar(ancho,alto)