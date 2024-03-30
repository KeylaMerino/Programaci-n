# Escritura de Archivo de Texto
# Creamos un archivo llamado my_notes.txt en modo de escritura ('w')
file = open('my_notes.txt', 'w')
# Escribimos algunas notas personales en el archivo
file.write("Nota 1: Recordar ir al supermercado.\n")
file.write("Nota 2: Llamar al médico para programar cita.\n")
file.write("Nota 3: Terminar el informe técnico antes del viernes.\n")
# Cerramos el archivo después de escribir
file.close()

# Lectura de Archivo de Texto
# Abrimos el archivo my_notes.txt en modo de lectura ('r')
file = open('my_notes.txt', 'r')
# Leemos el contenido del archivo línea por línea
for line in file.readlines():
    # Mostramos cada línea leída en la consola
    print(line.strip())
# Cerramos el archivo después de leer
file.close()