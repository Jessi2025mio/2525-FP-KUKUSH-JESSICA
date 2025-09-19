def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Función que calcula el monto de descuento aplicado a una compra.

    Parámetros:
    - monto_total (float): Monto total de la compra.
    - porcentaje_descuento (float): Porcentaje de descuento a aplicar (por defecto 10%).

    Retorna:
    - float: Monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal

# Primera llamada: solo se proporciona el monto total (usa el descuento por defecto)
monto1 = 250.00
descuento1 = calcular_descuento(monto1)
total1 = monto1 - descuento1

# Segunda llamada: se proporciona monto total y porcentaje personalizado
monto2 = 400.00
porcentaje2 = 15
descuento2 = calcular_descuento(monto2, porcentaje2)
total2 = monto2 - descuento2

# Salida de resultados
print("🧾 Resultados de la compra 1:")
print(f"Monto original: ${monto1:.2f}")
print(f"Descuento aplicado (10%): ${descuento1:.2f}")
print(f"Total a pagar: ${total1:.2f}")

print("\n🧾 Resultados de la compra 2:")
print(f"Monto original: ${monto2:.2f}")
print(f"Descuento aplicado ({porcentaje2}%): ${descuento2:.2f}")
print(f"Total a pagar: ${total2:.2f}")