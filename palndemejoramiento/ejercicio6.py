""""
metodos con condicionales 
hacer un programa que pida 2 numeros y se de cuenta cual de ellos es par 
o si ambos lo son 
"""
# pedimos al ususiaro que ingrese 2 numeros 
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

# aca realizamos la operacion para hallar cual es par o si ambos lo son 
if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("ambos numeros son enteros")
elif numero1 % 2 == 0 and numero2 % 2 != 0:
    print(f"{numero1} es par")
elif numero1 % 2 != 0 and numero2 % 2 == 0:
    print(f"{numero2} es par")
else:
    print("ambos numeros son impares")# por ultimo agregamos un else para decirle al usuario que los dos numeros que digito son impares