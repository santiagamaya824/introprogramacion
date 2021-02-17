numeroA = 4
numeroB = 6
pregunta_cualEsMayor = " el numeroA es mayor"
isMayorA = numeroA >= numeroB
print(pregunta_cualEsMayor)
print(isMayorA)

pregunta_AporB = "el numeroA multiplicadao por el numeroB es igual a 24?"
isMultiplicadoAporB = numeroA * numeroB >= 24
print(pregunta_AporB)
print(isMultiplicadoAporB)
print(numeroA * numeroB, "es el resultado de multiplicar el numero a por b")

#-----constantes-----#
PREGUNTA_numeroA = "cual es el numero A que quieres operar?  :  "
PREGUNTA_numeroB = "cual es el numero B que quieres operar?  :  "
MENSAJE_SUMA = "la suma de A+B es igual a : "
MENSAJE_RESTA = "la resta de A-B es igual a : "
MENSAJE_MULTIPLICACION = "la multiplicacion de A*B es : "
MENSAJE_DIVISION = "la division de A/B es : "
MENSAJE_EXPONENTE = "el exponente de A**B es : "

#preguntas para el usuario

print ("#"*15,"operaciones con numeros enteros", "#"*15)

#en la siguiente entrada de codigos solo se permiten numeros enteros

#-----entrada al codigo-----#
numeroA = int(input(PREGUNTA_numeroA))
numeroB = int(input(PREGUNTA_numeroB))
ismayorA = numeroA >= numeroB
print ("la ecuacion de A >= a B es", ismayorA)
print (MENSAJE_SUMA, numeroA + numeroB)
print (MENSAJE_RESTA, numeroA - numeroB)
print (MENSAJE_MULTIPLICACION, numeroA * numeroB)
print (MENSAJE_DIVISION, numeroA / numeroB)
print (MENSAJE_EXPONENTE, numeroA ** numeroB)

print ("#"*15,"operaciones con numeros decimales", "#"*15)

#en la siguiente entrada de codigos solo se permiten numeros decimales

#-----entrada al codigo-----#
numeroA = float(input(PREGUNTA_numeroA))
numeroB = float(input(PREGUNTA_numeroB))
ismayorA = numeroA >= numeroB
print ("la ecuacion de A >= a B es", ismayorA)
print (MENSAJE_SUMA, numeroA + numeroB)
print (MENSAJE_RESTA, numeroA - numeroB)
print (MENSAJE_MULTIPLICACION, numeroA * numeroB)
print (MENSAJE_DIVISION, numeroA / numeroB)
print (MENSAJE_EXPONENTE, numeroA ** numeroB)


