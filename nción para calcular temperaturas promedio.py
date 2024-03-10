def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcular la temperatura promedio de una ciudad durante un período de tiempo.

    Args:
    - datos_temperaturas (list): Una lista de listas que contiene los datos de temperaturas.
      Cada lista interna representa las temperaturas de una ciudad para varias semanas.

    Returns:
    - list: Una lista que contiene la temperatura promedio de cada ciudad.
    """
    temperatura_promedio_por_ciudad = []

    for ciudad_temperaturas in datos_temperaturas:
        promedio_ciudad = sum(ciudad_temperaturas) / len(ciudad_temperaturas)
        temperatura_promedio_por_ciudad.append(promedio_ciudad)

    return temperatura_promedio_por_ciudad

# Ejemplo de uso:
datos_temperaturas = [
    [25, 28, 24, 26],  # Temperaturas de la Ciudad 1 durante 4 semanas
    [22, 24, 23, 25],  # Temperaturas de la Ciudad 2 durante 4 semanas
    [28, 26, 27, 25]   # Temperaturas de la Ciudad 3 durante 4 semanas
]

resultados = calcular_temperatura_promedio(datos_temperaturas)
print("Temperatura Promedio por Ciudad:", resultados)