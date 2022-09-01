"""
    hacer un programa para sumar numeros pares dentro de un rango
    del 2 al 30
"""

a = int(input("Digite de donde va a comenzar a sumar?: "))
b = int(input("Digite hasta donde quiere llegar a sumar: "))
suma = 0

for i in range(a,b+1):
    if i %2==0: #si el numero es par
        suma +=i
print("la suma es: {}".format(suma))