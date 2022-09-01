def multiplicar(num1,num2): #parametros son aquellos dentro de los ()
    mult = num1 * num2
    return mult

#print(multiplicar(3,4))

mult = multiplicar(3,4)
print(mult)

#retorno de Valores multiples
def prueba():
    return "hola",12,[1,2,3]
print(prueba())

#2
def prueba():
    return "hola",12,[1,2,3]
s,n,l = prueba()
print(s)
print(n)
print(l)