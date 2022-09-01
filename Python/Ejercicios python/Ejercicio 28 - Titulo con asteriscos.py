"""
    Realizar un programa que cambie los espacios de una cadena por asteriscos y ademas cada palabra comienze por mayusculas
"""

cadena = input("Escribe algo: ")

cadena = cadena.replace(" "," , ")
cadena = cadena.capitalize()

print(cadena)