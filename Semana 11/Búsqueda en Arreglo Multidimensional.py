# Programa 1: Búsqueda en Arreglo Multidimensional

# Matriz bidimensional (3x3)
matriz = [
    [3, 6, 1],
    [7, 2, 9],
    [8, 5, 4]
]

# Valor que estamos buscando
valor_buscado = 2

# Inicializar variables para rastrear la posición del valor
fila_encontrada = -1
columna_encontrada = -1

# Recorrer la matriz para buscar el valor
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break  # Detener la búsqueda al encontrar el valor
    if fila_encontrada != -1:
        break  # Salir del bucle exterior si ya se encontró el valor

# Verificar si se encontró el valor y mostrar la posición
if fila_encontrada != -1:
    print(f"Se encontró {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")