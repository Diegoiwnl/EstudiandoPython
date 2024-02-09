ancho = int(input("Por favor ingrese el ancho del rectángulo: "))
altura = int(input("Por favor ingrese la altura del rectángulo: "))
caracter = input("Ingrese el carácter a utilizar: ")

def dibujar(an,al,letra):
    for i in range(an):
        for j in range(al):
            print(letra,end=" ")
        print()

dibujar(ancho,altura,caracter)