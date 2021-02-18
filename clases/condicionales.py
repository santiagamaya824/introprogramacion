# condicionales if = si, entonces y elif = si no, entonces 
# si no se cumple el if se cumpe elif y si no se cumple los dos enotnces es porque son iguales que seria else 
#......constantes.......#
mensaje_bienvenida = "hola, espero este bien"
mensaje_mayor = "el numeroA es mayor a numeroB"
mensaje_menor= "el numeroA es menor a numeroB"
mensaje_igual = "numeroA y numeroB son iguales"
pregunta_numeroA = "ingrese un numero A : "
pregunta_numeroB = "ingrese un numero B : "

#......entreda codigo......#
print (mensaje_bienvenida)
numeroA = int(input(pregunta_numeroA))
numeroB = int(input(pregunta_numeroB))
isMayor = numeroA > numeroB
isMenor = numeroA < numeroB
resultado = ""

if(isMayor):
    print(mensaje_mayor)
    resultado = mensaje_mayor
elif(isMenor):
    print(mensaje_menor)
    resultado = mensaje_menor
else:
    resultado = mensaje_igual

print(resultado)


