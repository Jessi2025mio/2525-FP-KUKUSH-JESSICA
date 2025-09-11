def calcular_promedio_temperaturas(lista_ciudades, datos_temperaturas):
    """
    Calcula el promedio de temperatura para cada ciudad durante varias semanas y días.

    Parámetros:
    - lista_ciudades (list): Nombres de las ciudades.
    - datos_temperaturas (list of lists of lists): Temperaturas organizadas por ciudad, semana y día.

    Retorna:
    - dict: Diccionario con ciudad como clave y temperatura promedio total como valor.
    """
    resultado_promedios = {}

    for ciudad, datos_por_ciudad in zip(lista_ciudades, datos_temperaturas):
        suma_total = 0
        total_registros = 0

        # Recorrer semanas y días para sumar las temperaturas
        for semana_datos in datos_por_ciudad:
            for temp_dia in semana_datos:
                suma_total += temp_dia
                total_registros += 1

        # Calcular promedio total para la ciudad
        promedio_ciudad = round(suma_total / total_registros, 2)
        resultado_promedios[ciudad] = promedio_ciudad

    return resultado_promedios


# ---
# Ejemplo de uso con datos de 3 ciudades y 4 semanas
ciudades = ["Ambato", "Tena", "Loja"]
temperaturas = [
    [
        [15, 16, 14, 13, 14, 15, 15],  # Semana 1 Ambato
        [14, 15, 15, 14, 13, 14, 15],  # Semana 2 Ambato
        [16, 14, 15, 16, 14, 15, 14],  # Semana 3 Ambato
        [15, 15, 16, 14, 15, 15, 16]   # Semana 4 Ambato
    ],
    [
        [24, 25, 26, 24, 23, 25, 26],  # Semana 1 Tena
        [25, 26, 27, 25, 24, 25, 26],  # Semana 2 Tena
        [26, 27, 28, 27, 26, 25, 27],  # Semana 3 Tena
        [27, 26, 25, 26, 27, 28, 26]   # Semana 4 Tena
    ],
    [
        [20, 21, 20, 19, 18, 19, 20],  # Semana 1 Loja
        [19, 20, 20, 19, 18, 18, 19],  # Semana 2 Loja
        [18, 19, 18, 17, 18, 19, 20],  # Semana 3 Loja
        [20, 19, 20, 21, 22, 20, 19]   # Semana 4 Loja
    ]
]

# Calcular promedios totales
promedios_totales = calcular_promedio_temperaturas(ciudades, temperaturas)

print("Temperatura promedio total por ciudad:")
for nombre_ciudad, promedio in promedios_totales.items():
    print(f"{nombre_ciudad}: {promedio}°C")

# Mostrar también promedio semanal para verificar
print("\nTemperatura promedio semanal por ciudad:")
for nombre_ciudad, temperaturas_por_ciudad in zip(ciudades, temperaturas):
    print(f"\nCiudad: {nombre_ciudad}")
    for idx_semana, temperaturas_semana in enumerate(temperaturas_por_ciudad, start=1):
        promedio_semanal = sum(temperaturas_semana)/len(temperaturas_semana)
        print(f"  Semana {idx_semana}: {promedio_semanal:.2f}°C")

