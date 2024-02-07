nalturas = int (input("Ingresar el numero de alturas deseadas: "))
suma = 0
promedio = 0 
contador = 0

while contador < nalturas:
    altura = float(input("Ingresar altura: "))
    suma = suma+altura
    promedio = suma/nalturas
    contador = contador+1

print ("El promedio de las alturas registradas es: " ,promedio)   