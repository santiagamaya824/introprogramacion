#-----punto1------#
import matplotlib.pyplot as plt
import pandas as pd 

alimento1 = input ("ingresa tu alimeto preferido : ")
precio1 = int(input("ingresa el precio del alimeto : "))
alimento2 = input ("ingresa tu alimeto preferido : ")
precio2 = int(input("ingresa el precio del alimeto : "))
alimento3 = input ("ingresa tu alimeto preferido : ")
precio3 = int(input("ingresa el precio del alimeto : "))
alimento4 = input ("ingresa tu alimeto preferido : ")
precio4 = int(input("ingresa el precio del alimeto : "))
aliemto5 = input ("ingresa tu alimeto preferido : ")
precio5 = int(input("ingresa el precio del alimeto : "))
alimento6 = input ("ingresa tu alimeto preferido : ")
precio6 = int(input("ingresa el precio del alimeto : "))
alimento7 = input ("ingresa tu alimeto preferido : ")
precio7 = int(input("ingresa el precio del alimeto : "))
alimento8 = input ("ingresa tu alimeto preferido : ")
precio8 = int(input("ingresa el precio del alimeto : "))

listaAlimentos = [alimento1,alimento2, alimento3, alimento4, aliemto5,alimento6,alimento7,alimento8]
listaPrecio = [precio1, precio2, precio3, precio4, precio5, precio6, precio7, precio8]

plt.bar(listaAlimentos,listaPrecio)
plt.xlabel("alimento")
plt.ylabel("precio")
plt.title("grafico barras")
plt.savefig ("barras.png")
plt.show()

#-----punto2------#
class Humano ():
    """
        Esta es la clase Humano exige atributos
        nombreEntrada: Hace referencia al nombre del usuario
        edadEntrada: Hace referencia al edad del usuario
        sexoEntrada: Hace referencia al sexo del usuario
        Tiene las siguientes acciones:
        * hablar (mensaje):
            dado un mensaje lo muestra en pantalla
        
        * mostrarAtributos ()
            muestra los atributos del usuario
    """
    def _init_(self, NombreEntrada, SexoEntrada, EdadEntrada):
        self.Nombre = NombreEntrada
        self.Sexo = SexoEntrada
        self.Edad = EdadEntrada
    def Hablar (self, Mensaje):
        print (Mensaje)

Humano1 = Humano ( "santiago", "Masculino", 20)
Humano1.Hablar ("me gusta salir y amanecer, beber y enloquecer, hasta que la noche termine")

class Doctor (Humano):
    def  __init__ ( self , estaturaEntrada, pesoEntrada ):
        self . estatura = estaturaEntrada
        self . peso = pesoEntrada
    
    def IMC (peso,estatura):
        imc = peso/(estatura**2)
        return imc

peso = float(input("ingrese su peso : "))
estatura = float(input("ingrese su estaura : "))

tu_imc = peso/(estatura**2)
print ("su imc es : ", tu_imc)

#-----punto3------#
repeticionCiclos = 1

while (repeticionCiclos == 1):
    try:
        nombre = str(input("ingresa tu nombre: "))
        assert (nombre.isalpha())
        repeticionCiclos = 2
    except AssertionError:
        print ("ingresaste un dato invalido, compruebe nuevamente")

while (repciclos == 2):
    try:
        dinero_dolares = int(input("cuanto dinero tienes en dolares"))
        repciclos = 3
    except ValueError:
        print ("dato invalido, compruebe nuevamente")

print(f"mi nombre es : " [nombre], "y tengo : " [dinero_dolares], "dolares" )

#-----punto4----#
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
Archivo.write ("=======\n")
Archivo.close()

