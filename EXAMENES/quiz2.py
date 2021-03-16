#---- quiz 2 -----#

Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

#----preguntas-----#

preguntaNumero  = """Ingrese alguna de estas opciones
    1.Hacer conversión de celsius a kevin o farenheit
    2.mostar lista clasificacion de temperatura
    3.Mostrar temperatura mas alta, más baja y cada cuanto se tomo la temperatura
    4.Salir
"""

tipoTemperatura  = """ respuesta en mayuscula
    C - Mostrar original en celsius
    K - Mostrar en kelvin
    F - Mostrar en farenheit
"""
preguntaTemperatura = " cual es la temperatura del paciente : "

#---convercion----#

listaKelvin = []
for elemento in Temperatura_Corporal :
    conversor = round(elemento + 273.15)
    listaKelvin.append (conversor)
listaFarenheit = []
for elemento in Temperatura_Corporal:
    conversor = round ((elemento * 1.8)+32)
    listaFarenheit.append (conversor)

#---entradas---#
print("bienvenido al codigo")

opcionesEscogida = int(input(preguntaNumero))
while (opcionesEscogida != 4):
    #----opcion1----#
    if (opcionesEscogida == 1):
        opcionTemperatura = (input(tipoTemperatura))
        if (opcionTemperatura == "C"):
            print("no es necesaria la convercion, ya su lista esta en celsius")
            print(Temperatura_Corporal)
        elif(opcionTemperatura == "K"):
            print("mostrando lista en grados kelvin")
            print(listaKelvin)
        elif(opcionTemperatura == "F"):
            print("mostrando lista en grados farenheit")
            print(listaFarenheit)
        else:
            print("el valor ingresado no es valido")
    #-----opcion2----#
    elif (opcionesEscogida == 2):
        temperatura = float(input(preguntaTemperatura))
        if(temperatura < 36):
            print("tienes hipotermia")
            print("su temperatura es : ", temperatura)
        elif(temperatura >= 36 and temperatura < 37.5 ):
            print("tienes una temperatura normal")
            print("su temperatura es : ", temperatura)
        else:
            print("tienes fiebre")
            print("su temperatura es : ", temperatura)
    #------opcion3----#
    elif (opcionesEscogida == 3):
        print( "esta es la temperatura mayor de la lista : " , max ( Temperatura_Corporal ))
        print("esta es la temperatura menor de la lista : " , min ( Temperatura_Corporal ))
        print("la temperatura se toma cada : ", len (Temperatura_Corporal ) / 24, "horas")
    #------opcion4-----#
    else:
        print("opcion invalida")
    opcionesEscogida = int(input(preguntaNumero))

print("gracias por interactuar con nosotros")
