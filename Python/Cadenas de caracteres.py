#se puede poner  cadenas dentro de cualquier tipo de comillas

cadena = 'Hola'
cadena2 = " hola 'saludos' " #comillas combinadas
cadena3 = "hola \"saludos\"" #comillas del mismo tipo
cadena4 = "hola  \n\tsaludos" #salto de linea y un espaciado de 4
cadena5 = r"D:\nombre\trabajos" #texto en crudo, es decir no procesa
cadena6 = """ hola """ #texto en varias lineas
cadena7 = "saludos"
cadena7 = 'a' + cadena7[1:] #agregar letras a las cadenas
cadena8 = "hola".upper() #pasar todo a mayuscula
cadena9 = "hola".lower() #pasar todo a minuscula
cadena10 = "hola".capitalize() #poner a mayuscula la 1ra letra
cadena11 = "hola".count('o') #contar cuatas veces se repite un caracter
cadena12 = "hola hola hola".find("hola") # ver donde se ubica un caracter o serie de caracteres
cadena13 = "1000".isdigit() #ves si una cadena tiene numeros
cadena14 = "aña".isalpha()  #ver si una cadena tiene solo letras
cadena15 = "jhon117".isalnum() #ver si una cadena es alpha numero
cadena16 = "saludos".islower() #ver si toda la cadena esta en minuscula
cadena17 = "SALUDOS".isupper() #ver si toda la cadena esta en mayuscula
cadena18 = "Saludos".istittle() #ver si la letra inicial es mayuscula
cadena19 = "       ".isspace()  #ver si la cadena está conformada por espacio
cadena20 = "hola".startswith('h') #ver con que letra empieza la cadena
cadena21 = "hola".endswith('a') #ver con que letra termina tu cadena
cadena22 = "hola mundo".split() #crea una lista
cadena23 = ",".join("jorge") #separar caracteres de una cadena
cadena24 = "   hola   ".strip() #eliminar espacios de una cadena
cadena25 = "hola owo".replace('o','0') #reemplazar un caracter por otro