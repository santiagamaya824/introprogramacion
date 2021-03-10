nombres = []
print (type(nombres))
print(nombres)
nombres = ['Santi','Samuel','Aleja','Elsa']
print (nombres)
print (nombres[2])
nombres.append('Mauricio')
print (nombres)
print (nombres[2])
edades = [18,19,20,17,32,14,13,12,15,16]
estaturas = [1.62,1.80,1.67,1.98]
#al último
print(edades[-2])
print(edades[0:2])
print(edades[:3])
print(edades[2:])
print(edades[:])
print(edades)
edades.sort()
print(edades)
edades.sort(reverse=True)
print(edades)
mayor = max(edades)
print (mayor)
menor = min(edades)
print (menor)
#como contamos cuantos elementos hay?
largoListaEdades = len(edades)
print (largoListaEdades)
#como sumamos elementos?
sumaEdades = sum(edades)
print (sumaEdades)
#como calculo el promedio
promedioEdades = sumaEdades/largoListaEdades
print (promedioEdades)
#eliminar un elemento
edades.pop(2)
print(edades)