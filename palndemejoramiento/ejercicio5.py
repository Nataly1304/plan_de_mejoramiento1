"""
una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente 
desea saber cuanto debera pagar finalmente por su compra 
"""
# pedimos al ususiario que ingrese el valor de su compra 
precio = float(input("digite el precio compra:"))

# realizamos el descuento y precio total de la compra 
descuento = precio * 0.15
precioTotal = precio - descuento 

# por ultimo le mostramos al usuario cuanto deberia de cancelar por su compra 
print(f"el precio total a pagar es: {precioTotal:.2f} ")