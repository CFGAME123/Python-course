"""
    Hacer un programa que pida un caracter e indique si es una vocal o no.
"""

letra = input("Escribe una letra: ").lower() #este metodo nos sirve para transformar caracteres a minuscula, es decir si lo escribimos en mayuscula lo va a pasar a minuscula, se puede hacer lo siguiente  tambien "letra=letra.lower()"

#tambien existe el upper() que es lo contrario al lower() es decir, pasa las minusculas a mayusculas seria algo asi "letra = input("Escribe una letra: ").upper()"


if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("es una vocal")
else:
    print("no es una vocal")