"""""
construir un programa que simule el funcionamiento de una calculadora que 
puede realizar las 4 operaciones aritmeticas basicas (suma, resta, multiplicacion
y division)el uso debe especificar la operacion con el primer caracter del nombre
de la operacion 
S,s-suma
R,r-resta
P,P,M,m-multiplicacion
D,d-division 
"""
# pedimos al usuario que digite 2 numeros 
numero1= float(input("digite un numero:"))
numero2= float(input("digite otro numero:"))

# pedimos al usuario que ingrese una opreacion aritmetica basica solo escriniendo la inicial de cada operacion 
operacion= input("\ningrese la operacion:")

# realizamos el debido proceso de la operacion utilizando el metodo upper para que al digitar nuestras letras las pueda utilizar en mayuculas o minusculas  
if operacion.upper()=='S':
    suma= numero1+numero2
    print(f"\nla suma es: {suma}")
elif operacion.upper()=='R':
    resta= numero1-numero2
    print(f"\nla resta es: {resta}")
elif operacion.upper()=='M' or operacion.upper()=='P':
    multiplicacion= numero1*numero2
    print(f"\nla multiplicacion es: {multiplicacion:.2f}")
elif operacion.upper()=='D':
    division= numero1/numero2
    print(f"\nla division es: {division}")
else:
    print("no es valida la operacion")# colocamos un else para determinar cuando una operacion no es valida 






