"""
Un programa con las operaciones basicas y complejas de aritmetica
"""

#Definir las variables
num1= float(input("Ingrese un numero:  "))
num2= float(input("Ingrese el siguiente numero:  "))

#sumar
suma= num1+ num2
print(suma)

#Resta
resta= num1 - num2

#Multiplicacion
multiplicacion= num1* num2

#Divison
division= num1
if num2 != 0:
    division = num1 / num2
else:
    print("ERROR: No se puede dividir entre cero")

#Potencia
potencia = num1 ** num2

#Radicacion
radicacion = num1 ** (1/num2)

print (f"El resultado de la suma es: '{suma}'")
print (f"El resultado de la resta es: '{resta}'")
print (f"El resultado de la multiplicacion es: '{multiplicacion}'")
print (f"El resultado de la division es: '{division}'")
print (f"El resultado de la potencia es: '{potencia}'")
print (f"El resultado de la radicacion es: '{radicacion}'")


