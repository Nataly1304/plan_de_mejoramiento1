# hacer un programa que pida 3 numeros y determine cual es el mayor 

# pedimos al usuario que ingrese 3 numeros 
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese un tercer numero: "))

# realizamos el debido proceso para hallar cual de los 3 numeros es el mayor 
if numero1>=numero2 and numero1>=numero3:
    print(f"el numero mayor es:{numero1:.0f}")
elif numero2>=numero1 and numero2>=numero3:
    print(f"el numero mayor es:{numero2:.0f}")
elif numero3>=numero1 and numero3>=numero2:
    print(f"el numero mayor es:{numero3:.0f}")