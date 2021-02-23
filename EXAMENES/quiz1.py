#Quiz 1 condicionales
#......constante......#
mensaje_bienbenida = "este es el resultado del examen"
pregunta_triglicerido = "ingrese el nivel de trigliceridos : "
pregunta_homocisteina = "ingrese el nivel de homocisteina : "
mensaje_despedida = "estos fueron los resultados de tu consulta, muchas gracias"

#......entrada codigo......#
print(mensaje_bienbenida)
trigliceridos = float(input(pregunta_triglicerido))
print("resultado de trigliceridos : ")
isOptimo = trigliceridos < 150
isSobreLimite = trigliceridos >= 150 and trigliceridos < 200
isAlto = trigliceridos >= 200 and trigliceridos < 500
isMuyAlto = trigliceridos >= 500

if(isOptimo):
    print("el nivel de trigliceridos esta en buenas condiciones")
elif(isSobreLimite):
    print("ten cuidado tus trigliceridos estas sobre el limite")
elif(isAlto):
    print("cuida de tu salud, tienes los trigliceridos altos")
else:
    print("cuidado, tus trigliceridos estan muy altos, corres peligro")

homocisteina = float(input(pregunta_homocisteina))
print("resultado de homocisteina : ")
isOptimoH = homocisteina >= 2 and homocisteina < 15
isSobreLimiteH = homocisteina >= 15 and homocisteina < 30
isAltoH = homocisteina >= 30 and homocisteina < 100
isMuyAltoH = homocisteina >= 100

if(isOptimoH):
    print("tu nivel de homocisteina esta optimo")
elif(isSobreLimiteH):
    print("ten cuidado, tu nivel de homocisteina esta sobre el limite")
elif(isAltoH):
    print("cuida tu salud, tienes el nivel de homocisteina alto")
else:
    print("cuidado, tu nivel de homocisteina estan muy altos, corres peligro")

print(mensaje_despedida)