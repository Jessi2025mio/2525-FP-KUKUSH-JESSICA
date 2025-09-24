# Tarea: Trabajando con Diccionarios en Python
# Objetivo: Utilizar diccionarios en Python para representar información estructurada y realizar operaciones comunes.

# ---------------------------------------------------------
# Paso 1: Crear un Diccionario
# Creamos un diccionario con información ficticia de una persona, en el orden solicitado.
informacion_personal = {"nombre": "Carolina Pérez", "edad": 30, "ciudad": "Guayaquil", "profesion": "Ingeniera",
                        "ocupacion": "Desarrollador de Software"}

# ---------------------------------------------------------
# Paso 2: Acceder y Modificar Valores
# Modificamos el valor de la clave "ciudad"

# Agregamos una nueva clave-valor relacionada con la ocupación (se agregará al final)

# ---------------------------------------------------------
# Paso 3: Verificar Existencia de Claves
# Verificamos si existe la clave "telefono", si no, la agregamos
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0991234567"

# ---------------------------------------------------------
# Paso 4: Eliminar una Clave
# Eliminamos la clave "edad" porque ya no es necesaria
del informacion_personal["edad"]

# ---------------------------------------------------------
# Paso 5: Imprimir el Diccionario Final
# Mostramos primero las claves en el orden solicitado
orden_claves = ["nombre", "ciudad", "profesion", "ocupacion", "telefono"]
print("Diccionario final ordenado según instrucción:")
for clave in orden_claves:
    if clave in informacion_personal:
        print(f"{clave}: {informacion_personal[clave]}")
