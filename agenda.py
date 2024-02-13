def registrar():
    #definimos el diccionario
    agenda={}
    respuesta = "s"

    while respuesta =="s":
        fecha = input("Por favor ingrese la fecha con formato D/M/A: ")
        lista=[]
        while respuesta =="s":
            hora = input("Ingresar la hora de la actividad con formato H/M: ")
            actividad = input("Ingresar el nombre de la actividad: ")
            lista.append((hora,actividad))
            respuesta = input("¿Desea ingresar otra actividad para la misma fecha? n/s: ")
        agenda[fecha]=lista
        respuesta = input("¿Desea ingresar una nueva fecha? n/s: ")
    return agenda

def mostar(agenda):
    print("Listado de la agenda")
    #recorrer la lista, inicia en fecha acaba en el final de la agenda
    for fecha in agenda:
        print("Para la fecha: ",fecha)
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
def consultarxfecha(fecha):
    fecha = input("Ingresar la fecha que desea consultar: ")
    if fecha in agenda:
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
    else:
        print("No existen actividades para la fecha ingresada")
agenda=registrar()
mostar(agenda)
consultarxfecha(agenda)