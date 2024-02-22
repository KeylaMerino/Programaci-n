# Programa de Búsqueda en Arreglo Multidimensional

def buscar_valor(matriz, valor):
    # Recorre la matriz para buscar el valor
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:
                return True, (i, j)  # Retorna True y la posición si se encuentra el valor

    return False, None  # Retorna False si no se encuentra el valor

def imprimir_matriz(matriz):
    # Imprime la matriz de forma legible
    for fila in matriz:
        print(fila)

# Matriz de ejemplo
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_a_buscar = 7

# Realizar la búsqueda
encontrado, posicion = buscar_valor(matriz_ejemplo, valor_a_buscar)

# Imprimir la matriz
print("Matriz:")
imprimir_matriz(matriz_ejemplo)

# Mostrar el resultado de la búsqueda
if encontrado:
    print(f"El valor {valor_a_buscar} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")