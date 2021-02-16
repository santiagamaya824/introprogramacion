#......contexto.....#
pregunta_peso = "cuanto pesas en kg? : "
pregunta_estatura = "cuanto mides en mts? : "
mensaje_bienvenida = " hola como estas? voy a calcular tu IMC"
mensaje_despedida = "tu IMC es ..."

#......entrada de codigo......#
print (mensaje_bienvenida)
peso = float (input (pregunta_peso))
estatura = float (input (pregunta_estatura))
imc = peso/(estatura**2)
print (mensaje_despedida, imc)
isObeso = imc >= 30
print("tu resultado de la prueba de obesidad es ...",isObeso)