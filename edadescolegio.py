cont1 = 0
cont2 = 0
cont3 = 0
tarde = 0
noche = 0
mañana = 0



for mañana in range (6):
    edad = int(input("Por favor ingrese las edades de la mañana: "))
    cont1 = cont1+edad
    promedio = cont1/6

for tarde in range (7):
    edad2 = int(input("Por favor ingrese las edades de la tarde: "))
    cont2 = cont2+edad2
    promedio2 = cont2/7

for noche in range (12):
    edad3 = int(input("Por favor ingrese las edades de la noche: "))
    cont3 = cont3+edad3
    promedio3 = cont3/12

print ("El promedio de edades de la jornadad de la mañana es: " ,promedio)
print ("El promedio de edades de la jornada de la tarde es: " ,promedio2)
print ("El promedio de edades de la jornada de la noche es: " ,promedio3)

if promedio > promedio2 and promedio > promedio3:
    print("Los estudiantes de la jornada mañana tienen mayor promedio de edad")
elif promedio2 > promedio and promedio2 > promedio3:
    print("Los estudiantes con mayor promedio de edad son de la jornada tarde")
else:
    print("Los estudiantes con mayor promedio de edad son de la jornada de la noche")