#juego con while e if 
#....constantes....#
saludo = "bienbenido, juguemos"
pregunta_numero = "en  este juego debes adivinar un numero q va del 1 al 10, lo puedes intentar las veces que quieras....exitos, ingresa tu numero : "
pregunta_fallaste = "fallaste, igresa otro numero : "
mensaje_ganaste = "felicidades ganaste"
mensaje_perdiste = "peridste, vuelve a intentarlo"

#...entrada codigo...#
numeroOculto = 7
vidas = 3
print(saludo)
numeroingresado = int(input(pregunta_numero))
if(numeroingresado != numeroOculto):
    vidas -=1
while (numeroOculto != numeroingresado and vidas >0):
    numeroingresado = int(input(pregunta_fallaste))
    vidas -=1

if (vidas >= 0 and numeroingresado == numeroOculto):
    print(mensaje_ganaste)
    print(vidas)
else:
    print(mensaje_perdiste,"el numero era el",numeroOculto)
