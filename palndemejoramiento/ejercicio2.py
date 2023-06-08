# determinar la solucion  logica de la siguiente operacion 

#pedimos al usuario asignar 2 valores para a y b 
a = float(input("escribe un valor a ="))
b = float(input("escribe un valor b ="))

#utilizamos la variable resultado para almacenar el valor de toda la operacion 
resultado = ((3+5*8)<3 and (-6/3*4)+2<2) or (a>b)

# ya por ultimo obtenemos el resultado dependiento de los valores que le asignamos
print("el resultado es:{resultado}")