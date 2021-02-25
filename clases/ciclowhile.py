#el while sirve para repetir una condicion hasta que se cumpla
#.....entrada.....#
saludo = "hola, te ayudare ahorrando"
mensaje_ahorro = "llevas ahorrado..."
pregunta_valor_cpu = "cuanto vale el pc? : "
pregunta_ahorro ="cuanto tienes ahorrado? : "

#.... entrada codigo...#
print(saludo)
valorCPU = float(input(pregunta_valor_cpu))
ahorrado = float(input(pregunta_ahorro))

while (valorCPU > ahorrado):
    print(mensaje_ahorro,ahorrado,"te faltan...",valorCPU - ahorrado)
    ahorrado = ahorrado +1000

print( valorCPU == ahorrado)

