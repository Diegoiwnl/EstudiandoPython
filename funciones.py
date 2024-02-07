def iniciouwu():
    print("MENÚ PRINCIPAL")
    print("Sleccione la opcion correcta: ")
    print("1 Opreación sumar")
    print("2 Operación resta")
    print("3 Opreación multiplicar")
    print("4 Operación dividir")
    print("5 Salir")
def main():
    while True:
        iniciouwu()
        opcion = int(input("Seleccione la opcion: "))
        if opcion == 1:
            print("Ha seleccionado la Suma")
            Num1 = int(input("Ingresar el primer numero: "))
            Num2 = int(input("Ingresar el segundo numero: "))
            Sumar = Num1+Num2
            print("El resultado de la suma es: " ,Sumar)
        elif opcion == 2:
            print("Ha seleccionado la operacion Resta")
            Num1 = int(input("Ingresar el primer numero: "))
            Num2 = int(input("Ingresar el segundo numero: "))
            restar = Num1-Num2
            print("El resultado de la resta es: " ,restar)
        elif opcion == 3:
            print("Ha seleccionado la operacion Multiplicar")
            Num1 = int(input("Ingresar el primer numero: "))
            Num2 = int(input("Ingresar el segundo numero: "))
            multiplicar = Num1*Num2
            print("El resultado de la resta es: " ,multiplicar)
        elif opcion == 4:
            print("Ha seleccionado la operacion Dividir")
            Num1 = int(input("Ingresar el primer numero: "))
            Num2 = int(input("Ingresar el segundo numero: "))
            Dividir = Num1/Num2
            print("El resultado de la resta es: " ,Dividir)
        elif opcion == 5:
            print("Nospi joven")    
            break
        else:
            print("Opcion no válida, seleccione una opción valida")

main()
