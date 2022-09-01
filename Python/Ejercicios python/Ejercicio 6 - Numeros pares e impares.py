"""
    Hacer un programa que pida 2 numeros y se de cuenta cual de ellos es par y cuales lo son
"""

numero1 = int(input("digita un numero: "))
numero2 = int(input("digita un numero mas: "))

if numero1%2==0 and numero2%2==0:
    print("ambos son pares")
elif numero1%2==0 and numero2%2!=0:
    print("numero 1 es par")
elif numero2%2==0 and numero1%2!=0:
    print("el numero 2 es par")
else:
    print("ambos numeros son impares")