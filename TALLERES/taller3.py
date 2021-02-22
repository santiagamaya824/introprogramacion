# ejercicios condicionales
print ("#"*15,"punto numero 1", "#"*15)
# PUNTO 1
#..... constantes.....#
mensaje_bienvenida = "bienvenido al codigo"
mensaje_mayorA = "el numeroA es mayor"
mensaje_mayorB = "el numeroB es mayor"
mensaje_igual = "los numeros son iguales"
numeroA = 3
numeroB = 3

#......entrada al codigo.....#
print(mensaje_bienvenida)
isMayorA = numeroA > numeroB
isMenorB = numeroA < numeroB

if(isMayorA):
    print(mensaje_mayorA)
elif(isMenorB): 
    print(mensaje_mayorB)
else:
    print(mensaje_igual)

print ("#"*15,"punto numero 2", "#"*15)
#PUNTO 2
#......constantes.....#
pregunta_edad = "cuantos años tienes ? : "
mensaje_Menor_Edad = "eres menor de edad"
mensaje_Joven = "eres joven, estas en tus mejores años"
mensaje_Adulto = "eres adulto"
mensaje_Adulto_Mayor = "eres de la tercera edad"

#.....entrada condigo....#
Edad = int(input(pregunta_edad))
isMenorEdad = Edad < 18
isJoven = Edad >= 18 and Edad < 25
isAdulto = Edad >= 26 and Edad < 60
isAdultoMayor = Edad >= 60
resultado = ""

if(isMenorEdad):
    resultado = mensaje_Menor_Edad
elif(isJoven):
    resultado = mensaje_Joven
elif(isAdulto):
    resultado = mensaje_Adulto
else:
    resultado = mensaje_Adulto_Mayor

print(resultado)

print ("#"*15,"punto numero 3", "#"*15)

# PUNTO 3
# preguntas para personas que ingresaron a la universidad
#.....constantes....#
pregunta_año = "ingresa el año actual : "
pregunta_año_ingreso_universidad = "ingresa el año en que entraste a la universidad : "
pregunta_año_grados = "ingresa el año en el cual debes de graduarte : "
mensaje_años_que_faltan = "años faltan para graduarte"
mensaje_años_que_pasaron = "años han pasado desde el ingreso a la universidad"

#...entrada codigo...#
Año = int(input(pregunta_año))
IngresoUniversidad = int(input(pregunta_año_ingreso_universidad))
GradoUniversidad = int(input(pregunta_año_grados))
isAñosQuePasaronDesdeIngreso = IngresoUniversidad - Año
isAñosQueFaltanParaGrados = GradoUniversidad - Año

if(isAñosQuePasaronDesdeIngreso):
    print(Año - IngresoUniversidad, mensaje_años_que_pasaron)

if(isAñosQueFaltanParaGrados):
    print(GradoUniversidad - Año, mensaje_años_que_faltan)

print ("#"*15,"punto numero 4", "#"*15)


#PUNTO 4
#......constantes.....#
pregunta_distancia = "escribe una distancia en centimetros : "
mensaje_kilometros = "distancia en kilometros"
mensaje_metros = "distancia en metros"
mensaje_centimetros = "distancia en centimetros"

#.....entrada codigo.....#
distancia = float (input(pregunta_distancia))
iskilometros = distancia * 10**-5
isMetros = distancia * 10**-2

if(iskilometros):
    print(distancia * 10**-5,mensaje_kilometros)

if(isMetros):
    print(distancia * 10**-2, mensaje_metros )










