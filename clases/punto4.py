NombreArchivo = "Paciente.txt"

Nombre = input ("Digite su nombre :")
Enfermedad = input ("Digite la enfermedad que está padeciendo :")
Precio = 0

try:
    Archivo = open (NombreArchivo)
except FileNotFoundError:
    Archivo = open (NombreArchivo, "w", encoding="UTF-8")
    DescripcionArchivo = "Archivo de pacientes neurologicos"
    Archivo.writelines (DescripcionArchivo)
    Archivo.close()

isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        ValorConsulta = int (input("Ingrese valor de su consulta: "))
        isCorrectInfo = True
    except ValueError:
        print ("Ingrese un dato no válido")

Archivo = open (NombreArchivo, "a", encoding = "UTF-8")
Archivo.write (f"Equipo : {Nombre}\n")
Archivo.write (f"Descripcion : {Enfermedad}\n")
Archivo.write (f"Precio : {ValorConsulta}\n")
Archivo.write ("=====\n")
Archivo.close()