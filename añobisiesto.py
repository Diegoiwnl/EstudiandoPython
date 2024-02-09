añousuario =  int(input("Por favor ingrese el año que desea xdxddxdx :v "))
aactual = 2024

def añobis(año):
    if (año % 4 == 0) and (año % 100 != 0):
        print("El año ingresado es un año bisiesto uwu")
    elif (año % 100 == 0) and (año % 400 == 0):    
        print("El año ingresado es un año bisiesto")
    else:
        print("El año ingresado no es un año bisiesto")

añobis(añousuario)
