# Registro de Temperaturas Diarias - Matriz 3D

# Ciudades registradas
ciudades = ["Coca", "Quito", "Loja"]

# Días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Matriz 3D: temperaturas[ciudad][semana][día]
temperaturas = [
    [  # Coca
        [28, 29, 30, 31, 30, 29, 28],  # Semana 1
        [27, 28, 29, 30, 29, 28, 27]   # Semana 2
    ],
    [  # Quito
        [22, 23, 21, 20, 19, 18, 20],  # Semana 1
        [21, 22, 20, 19, 18, 17, 19]   # Semana 2
    ],
    [  # Loja
        [19, 20, 18, 17, 16, 15, 17],  # Semana 1
        [18, 19, 17, 16, 15, 14, 16]   # Semana 2
    ]
]

# Mostrar promedio de temperaturas por ciudad y semana
for i in range(len(ciudades)):
    print(f"\n📍 Ciudad: {ciudades[i]}")
    for j in range(len(temperaturas[i])):
        suma = 0
        for k in range(len(temperaturas[i][j])):
            suma += temperaturas[i][j][k]
        promedio = suma / len(temperaturas[i][j])
        print(f"  Semana {j + 1}: Promedio = {promedio:.2f}°C")