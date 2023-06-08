""""
hacer un programa que simule un cajero automatico un saldo inicial 
de $1000 y tendra el siguente menu de opciones :
    
1-ingresar dinero en la cuenta 
2-retirar dinero de la cuenta 
3-mostrar dinero disponible 
4-salir
"""

saldo = 1000
print= ("\t.MENU.")#esta operacion nos sirve para darle un espcio a la palabra y quede como titulo 
print("1-ingresar dinero en la cuenta ")
print("2-retirar dinero de la cuenta ")
print("3-mostrar dinero disponible")
print("4-salir")
opcion= int(input(" digite una opcion:"))# le decimos al usuario que ingrese un numero de los que mostramos en el menu de opciones, correspondiente a lo que necesita 

print()#este print vacio nos sirve para dar un salto de linea 

# realizamos el menu de opciones  
if opcion==1:
    extra = float(input("cuanto dinero desea ingresar:"))
    saldo += extra
    print(f"dinero en la cuenta: {saldo}")
elif opcion==2:
    retirar = float(input("cuanto dinero desea retirar:"))
    if retirar>saldo:
        print("no tiene esa cantidad de dinero:")
    else:
        saldo-=retirar
        print(f"dineroen la cuenta: {saldo}")   
elif opcion==3:
    print(f"dinero en la cuenta: {saldo}")
elif opcion==4:
    print(f"gracias por la utilidad")
else: 
    print("eror,se equivoco")# ingresamos un else para informar eror 
    
