Persona = {
    "Nombre":"Diego",
    "Apellido":"Mesa",
    "Estatura": 1.61,
    "Edad" : 17,
    "Email" : "diegomesaglwh@gmail.com",
    "CiudadNac" : "Bogotá",
    "Género" : ["Femenino","Masculino","Otre"]

}

print(Persona)  
#Mostrar un elemento del comentario
print("El nombre de la persona es:" ,{Persona["Nombre"]})
#Agregar elemento
Persona["Teléfono"]=3205451321
print(Persona)
#Modificar elemento del diccionario
Persona["Teléfono"]=9999999999
print(Persona)
#Modificar clave del elemento
Persona["Celular"]=Persona.pop("Teléfono")
print(Persona)
#Eliminar un elemento del diccionario
del Persona["Celular"]
print(Persona)
#Integrar los ítems de las claves y valores
for clave,valor in Persona.items():
    print(clave," : ",valor )