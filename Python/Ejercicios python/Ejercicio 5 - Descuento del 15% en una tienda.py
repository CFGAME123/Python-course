"""
    Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debera pagar finalmente por su compra
"""

precio = float(input("escribe el precio: "))
descuento = precio * 0.15
final = precio - descuento
print("precio final es $$$: {} ".format(final))