# Programa 2: Ordenación de Arreglo Multidimensional

# Matriz bidimensional (3x3)
matriz = [
    [3, 6, 1],
    [7, 2, 9],
    [8, 5, 4]
]

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar cada fila de la matriz
for indice, fila in enumerate(matriz):
    bubble_sort(fila)

# Mostrar matriz después de ordenar todas las filas
print("\nMatriz después de ordenar todas las filas:")
for fila in matriz:
    print(fila)

