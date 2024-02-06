import random

Secreto = random.randint(1,10)

Numero = int(input("Adivine el número entre 1 y 10 "))

while Numero != Secreto:
    if Numero < Secreto:
        print("El número es mayor ")
    else:
        print("El número es menor ")

    Numero = int(input("Inténtalo de nuevo: "))

print("Felicitaciones adivinaste el número secreto: " ,Secreto)