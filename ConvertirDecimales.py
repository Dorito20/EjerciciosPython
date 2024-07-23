#escribir un prograqma que solicite el usuario ingresar un nmero
#con decimales y almacenarlo en una variable.
#A continuacion, el programa debe solicitar al usuario que ingrese
#un numero entero y guardarlo en otra variable.
#En una tercera variable se debera guardar el resultado de la suma 
#de los dos numeros ingresado por el usario.
#Por ultimo, se debe mostrar en pantalla el texto 
# "El resultado de la suma [suma]", donde "[suma]"
#se reemplazara por el resultado de la operacion.
 
valordecimal = float(input("Ingrese un decimal: "))
valorentero = int(input("Ingrese un entero: "))
suma = valordecimal + valorentero
print("El resultado de la suma:" ,suma)
#print("El resultado de la suma:" + str(suma))