# ejercicios condicionales
print ("#"*15,"punto numero 1", "#"*15)
# PUNTO 1
#..... constantes.....#
mensaje_bienvenida = "bienvenido al codigo"
mensaje_mayorA = "el numeroA es mayor"
mensaje_mayorB = "el numeroB es mayor"
mensaje_igual = "los numeros son iguales"
numeroA = 5
numeroB = 4

#......entrada al codigo.....#
print(mensaje_bienvenida)
isMayorA = numeroA > numeroB
isMayorB = numeroA < numeroB

if(isMayorA):
    print(mensaje_mayorA)
elif(isMayorB): 
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
pregunta_año_ingreso_universidad = "ingresa el año en que entraste o quieres ingresar a la universidad : "
mensaje_años_iguales = "los años que ingresaste son iguales"
mensaje_años_que_pasaron = "años han pasado desde el ingreso a la universidad"

#...entrada codigo...#
Año = int(input(pregunta_año))
IngresoUniversidad = int(input(pregunta_año_ingreso_universidad))

if(Año > IngresoUniversidad):
    print(Año - IngresoUniversidad,mensaje_años_que_pasaron)

elif(Año < IngresoUniversidad):
    print(IngresoUniversidad - Año, "años faltan para estar en la universidad")

else:
    print(mensaje_años_iguales)
print ("#"*15,"punto numero 4", "#"*15)

#PUNTO 4
#......constantes.....#
pregunta_distancia = "escribe una distancia en centimetros : "
pregunta_unidad = "escriba a que unidad quiere convertir la distancia : "
mensaje_kilometros = "es la distancia en kilometros"
mensaje_metros = "es la distancia en metros"
mensaje_milimetros = "es la distancia en milimetros"
mensaje_error = "tuviste un error, intentalo de nuevo"

#.....entrada codigo.....#
distancia = float (input(pregunta_distancia))
unidad = input(pregunta_unidad)
kilometros = distancia * 10**-5
metros = distancia * 10**-2
milimetros = distancia * 10

if(unidad == "kilometros"):
    print(kilometros,mensaje_kilometros)

elif(unidad == "metros"):
    print(metros, mensaje_metros)

elif(unidad == "milimetros"):
    print(milimetros,mensaje_milimetros)

else:
    print(mensaje_error)










