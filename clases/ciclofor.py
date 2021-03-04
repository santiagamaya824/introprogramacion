for iteracion in range (10):
    print (iteracion)
# en el anterior pone los numeros del 1 al 9
print ("#"*60)

for iteracion in range (10):
    print(iteracion + 1)
#en el anterior pone los numeros del 1 al 9 pero siempre a la iteracion le sumera 1 pa que llegue a 10
print ("#"*60)
for interacion in range (1,11):
    print(iteracion)
#en el anteior pone los numeros del 1 al 10 ya que se puso 11 en el rango
print("#"*60)

for iteracion in range (1,11,2):
    print( iteracion)
#en el anterior pone los numeros del 1 al 10 pero de 2 en 2 empezando desde el 1 
print("#"*60)

for iteracion in range (1,11): 
    if (iteracion % 2 == 0):
        print ( iteracion)
#en el anterior pone los numeros pares
print("#"*60)

for iteracion in range (1,11):
    if (iteracion % 2 == 0):
        print (iteracion, "es un numero par")
    else:
        print(iteracion,"es un numero impar")
#en el anterior pone los numeros par y cuales son impares
