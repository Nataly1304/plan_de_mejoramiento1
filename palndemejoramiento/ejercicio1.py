# escribir la suguiente expresion en forma de exprecion aritmetica 

#pedimos al usuario asignar 3 valores para a, b y c
a = float(input("dale un valor a =")) 
b = float(input("dale un valor b=")) 
c = float(input("dale un valor c="))

# ya despues que tengamos los 3 valores podemos sacar un determinado resltado de la expresion  

resultado= (a**3 * (b**2 - 2*a*c))/(2*b) # en esta expresion tenemos dos bloques numerador y denominador son bloques dividos por division 


# ya por ultimo obtenemos el resultado dependiento de los valores que le asignamos 
print(f"el serultado es: {resultado}")
