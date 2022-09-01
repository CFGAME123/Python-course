"""
    permite realizar expresiones logicas y permite un resultado de manera booleana
"""

"""
    and : conjuncion  : multiplicacion logica 
                        para tener un valor verdadero tenermos que tener 2 valores verdaderos es decir todo verdadero
    
    or  : disyuncion  : suma logica (1 sola expresion verdadera da como resultado verdadero)
    
    not : negacion    : negar un true = falso
                        negar un false = true
"""

a = 10
b = 12
c = 13
d = 10

resultado = ((a > b) or (a < c)) and ((a == c) or (a >= b))
print(resultado)

#ejercicio
a = 10
b = 15
c = 20

resultado2 = ((a<b) and (b<c))
print(resultado2)

resultado3 = ((a>b) or (b<c))
print(resultado3)

resultado2 = not ((a>b) or (b<c))
print(resultado2)