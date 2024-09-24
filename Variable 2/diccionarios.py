#Definicion de un diccionario
mi_diccionario = {
"nombre":"Miguel Perez",
"edad": 24,
"ciudad": "Cali",
"idioma": ["ingles", "español","frances"],
"Gruposanginio": None
}

#Acceder a un valor 
print(mi_diccionario["nombre"]) #Salida: Miguel Perez

#Modificar un valor 
mi_diccionario["edad"] = 27
print(mi_diccionario)

#Agregar un nuevo par de clave-valor
mi_diccionario["profesion"] = "ingeniero"
print(mi_diccionario)

#Eliminar un par de clave-valor
del mi_diccionario["ciudad"]
print(mi_diccionario)
