#hacer un programa que pida un caracter e indique si es una vocal o no 


letra = input("digite un caracter:").lower() # si colocamos el metodo lowwer aqui es mas facil por que pide al usuario que digite un caracter y va a transformar en minuscula y se guarda dentro de la variable letra 

if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
    print("es una vocal") 
else:
    print("no es una vocal")# agregamos un else para dar a entender al usuario que lo que digito no es una vocal 