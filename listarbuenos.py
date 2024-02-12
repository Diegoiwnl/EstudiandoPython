#definir las listas que vamos a trabajar
Nombres=[]
Notas=[]
Alumgod = []
mb = 0
b = 0
iN = 0

#Llenar la lista
for x in range(1,5):
    Nom = input(f"Por favor ingresar el nombre del alumno {x}: ")
    #Agregar el dato a la lista
    Nombres.append(Nom)
    Not = int(input(f"Por favor ingresar las notas del alumno {x}: "))
    #Agregar el dato a la lista
    Notas.append(Not)

#Recorrer la lista 
for y in range(len(Nombres)):
    print(Nombres[y])
    print(Notas[y])


if Notas[y]>=8:
        print("Eres buenardo mi loco")
        mb += 1
        Alumgod.append(Nombres[y])
else:
    if Notas[y] >=4:
        print("Bueno algo es algo viste ")
        b += 0
    else:
        print("Alumno no aprueba la materia")
        iN += 1
print("Listado inicial de los alumnos son: " ,Nombres)

#Mostrar los alumnos que son alumnos muy buenos
eliminar = []
for z in range (len(Notas)):
    if 4 <= Notas[z]<= 7:
         ##Notas.pop(z)
         ##Nombres.pop(z)
         eliminar.append(z)
for d in sorted(eliminar,reverse=True):
     Notas.pop[d]
     Nombres.pop[d]
    
print("La cantidad de alumnos muy buenos son: " ,mb)
print("El nombre de los mejores alumnos son:  " ,Alumgod)
print("Listado de alumnos eliminadaos son" ,Nombres)

