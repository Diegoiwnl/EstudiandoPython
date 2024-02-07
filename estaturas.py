def main():
    
    num_registros = int(input("Ingrese el número de registros de altura que desea hacer: "))
    
    
    suma_alturas = 0
    
    
    for i in range(num_registros):
        altura = float(input(f"Ingrese la altura {i + 1} en centímetros: "))
        suma_alturas += altura
    
    
    promedio_alturas = suma_alturas / num_registros
    
    
    print(f"El promedio de las alturas registradas en centimetros es: " ,promedio_alturas)


