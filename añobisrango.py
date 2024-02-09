
def añobisrange(año):

año1 = int(input("Por favor ingresar el primer año: "))
año2 = int(input("Por favor ingresar el segundo año: "))
cant_veces= año1-año2
cantbis = 0
catnobis = 0
for i in range (cant_veces):
        if (año1 % 4 == 0) and (año1 % 100 != 0):
            cantbis= cantbis + 1
        elif (año1 % 100 == 0) and (año1 % 400 == 0):    
            print("El año ingresado es un año bisiesto")
        cantbis= cantbis + 1
else:
        print("El año ingresado no es un año bisiesto")
        catnobis = catnobis +1

print("La cantidad de años bisiestos son: " ,cantbis)
print("La cantidad de años no bisietos son: " ,catnobis)

añobisrange(año1)