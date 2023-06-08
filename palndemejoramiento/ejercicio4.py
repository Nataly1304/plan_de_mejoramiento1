"""""
hacer un programa para ingresar el radio de un circulo y se reporte su area 
y la longitud de la circunferencia 
"""""

import math #aca estamos importando el valor de pi que se necesita para el area

# pedimos al ususario asignar un valor para el radio 
radio = float(input("radio->"))
# realizamos la operacion  
area = math.pi * radio**2
longitud = 2 * math.pi * radio
# y por ultimo ponemos los print para obtener resultados en la consola 
print(f"el area es: {area:.3f}")
print(f"el longitud de la circunferencia es: {longitud:.3f}")
