# Crear una matriz 3D para representar los datos de temperaturas
# Supongamos 3 ciudades, 7 días de la semana y 4 semanas
temperaturas = [[[0.0 for _ in range(7)] for _ in range(4)] for _ in range(3)]

# Llenar la matriz con datos de temperaturas aleatorias (puedes modificar esto según tus necesidades)
import random
for ciudad in range(3):
    for semana in range(4):
        for dia in range(7):
            temperaturas[ciudad][semana][dia] = random.uniform(20, 30)  # Temperaturas entre 20 y 30 grados Celsius

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in range(3):
    for semana in range(4):
        promedio_semana = sum(temperaturas[ciudad][semana]) / len(temperaturas[ciudad][semana])
        print(f"Promedio de temperaturas para la Ciudad {ciudad + 1}, Semana {semana + 1}: {promedio_semana:.2f}°C")




