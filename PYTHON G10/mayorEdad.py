nombre = str(input("Nombre:  "))
edad = int(input("Edad: "))
documento = str(input("Documento:  ")).lower()


if ((edad>=18) and (documento== "si")):
    print ("Puede entrar")
else:
    print ("No puede entrar")
    
    
