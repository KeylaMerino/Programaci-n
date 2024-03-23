# Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Victor",
    "edad": 28,
    "ciudad": "Berlín",
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Londres"

# Agregar una nueva clave-valor que represente la profesión
informacion_personal["profesion"] = "Ingeniero"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123456789"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario resultante
print("Información personal final:")
print(informacion_personal)