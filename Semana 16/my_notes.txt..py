# Tarea: Trabajo con Archivos de Texto en Python
# Esta actividad consiste en crear un archivo de texto, escribir notas personales,
# leerlas línea por línea y mostrar el contenido en consola.

# Escritura de Archivo de Texto
# Abrimos el archivo 'my_notes.txt' en modo escritura ('w') para crear o sobrescribir el archivo
archivo = open('my_notes.txt', 'w')

# Escribimos tres líneas de notas personales usando el método write()
archivo.write("Nota 1: Estudiar para el examen final de programación.\n")
archivo.write("Nota 2: Revisar los apuntes de la Unidad 4 sobre archivos.\n")
archivo.write("Nota 3: Subir la tarea al repositorio de GitHub antes del domingo.\n")

# Cerramos el archivo después de escribir
archivo.close()

# Lectura de Archivo de Texto
# Abrimos el archivo en modo lectura ('r') para leer su contenido
archivo = open('my_notes.txt', 'r')

# Leemos el contenido línea por línea usando readline() dentro de un bucle
linea = archivo.readline()
while linea:
    print(linea.strip())  # Mostramos la línea en consola sin el salto de línea
    linea = archivo.readline()

# Cerramos el archivo después de leer
archivo.close()
