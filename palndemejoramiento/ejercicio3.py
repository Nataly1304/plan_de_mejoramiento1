# hacer un programa para intercambiar el valor de 2 variables 

#pedimos al usuario asignar 2 valores para a y b 
a = input("escribe un numero para la variable a =")
b = input("escribe un numero para la variable b =")

a , b = b , a # esta forma no sirve para intercambiar los valores de ambas variables
 
# aca obtenos nuestros resultados 
print (f"el valor de a es: {a} ")
print (f"el valor de b es: {b} ")