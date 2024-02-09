texto = "Buenos días definiendo un parámetro en una función"

#funcion sin parámetros
def mensaje():
    N1 = int(input("Ingresar el primer número: "))
    N2 = int(input("Ingresar el segundo número: "))
    calcularmayor(N1,N2)
    positivo(N1,N2)

#funcion con parámetros
def calcularmayor(num1,num2):
    if num1>num2:
        print("El primer número es el mayor")
    elif num1==num2:
        print("Son números igules")
    else:
        print("El segundo número es el mayor")

def positivo(p1,p2):
    if p1>0 and p2>0:
        print("Los dos números ingresados son positivos")

    elif p1<0 and p2<0:
        print("Los dos números ingresados son negativos")
    else:
        print("Al menos uno de los números no es positivo")

mensaje()
