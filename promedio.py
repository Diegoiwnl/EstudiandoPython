cont = 0
Acum = 0


while cont < 10:
    Num = int(input("Ingresar el número: "))
    Acum=Acum+Num


    cont=cont+1
Promedio = Acum/10

print("La suma de los números es: " ,Acum)
print("El promedio de los 10 números es: ",Promedio)