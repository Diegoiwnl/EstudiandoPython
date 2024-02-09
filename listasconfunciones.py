def ingresar():
    enteros = []

    for x in range(5):
        num = int(input("Por favor ingrese el numero: "))
        enteros.append(num)
    imprimir(enteros)
    sumar(enteros)

def imprimir(enteros):
    print("Los datos de la lista son: ")
    for x in enteros:
        print(x)

def sumar (enteros):
    acum = 0
    for x in enteros:
        acum=acum+x
    print("La  suma de los elementos es: " ,acum)

ingresar()