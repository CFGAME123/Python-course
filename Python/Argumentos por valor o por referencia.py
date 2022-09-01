#argumentos por valor
def doblar_valor(numero):
    numero *= 2
n = 5
doblar_valor(n) #se le asigna una copia del valor de n, n no cambia su valor

#argumentos por referencia | cualquier modificacion afecta en la variable externa
def doblar_valor2(numero2):
    for i,n in enumerate(numeros):
        numero[i] *0 2

n2 = [5,10,15,20] 
doblar_valor2(n2) #(n[:]) | pasar coleccion por valor
print(n2)