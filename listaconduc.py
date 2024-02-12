NombreC = []
Kms = []
Totalkms =[]
KmAcum = []



Camioneros = int(input("Por favor ingrese la cantidad de conductores: "))

for x in range(Camioneros):
    Nombre = input("Por favor ingrese el nombre del conductor: " )
    NombreC.append(Nombre)
    KmAcum = 0
    
    for i in range(7):
        Km = int(input("Por favor ingrese la cantidad de Km: "))
        KmAcum = KmAcum + Km
    
    Totalkms.append(KmAcum)

print(NombreC,"Los kilometros recorridos son",Totalkms) 
