# Programa de Ordenación de Arreglo Multidimensional

def ordenar_fila(matriz, indice_fila):
    # Utiliza el método sort para ordenar la fila especificada
    matriz[indice_fila].sort()

# Matriz de ejemplo
matriz_ejemplo = [
    [9, 5, 3],
    [2, 8, 1],
    [7, 4, 6]
]

# Índice de la fila a ordenar
fila_a_ordenar = 1

# Imprimir la matriz original
print("Matriz Original:")
for fila in matriz_ejemplo:
    print(fila)

# Aplicar la ordenación a la fila especificada
ordenar_fila(matriz_ejemplo, fila_a_ordenar)

# Imprimir la matriz con la fila ordenada
print("\nMatriz con Fila Ordenada:")
for fila in matriz_ejemplo:
    print(fila)