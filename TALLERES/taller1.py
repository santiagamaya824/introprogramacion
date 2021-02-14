saludo = "hola mundo"
# datos personales 
nombre = "santiago amaya mendez"
edad = 20 
estaura = 1.71
peso = 70
pruebav = True
pruebaf = False
print ("#"*15," es menor de edad", "#"*15)
isMenorEdad = edad <=18
print(isMenorEdad)
print("su edad es", edad)
print ("#"*15," esta en sobre peso?", "#"*15)
isSobrePeso = peso >=110
print(isSobrePeso)
print("su peso es",peso)
print ("#"*15," tiene altura promedio", "#"*15)
isEstauraPromedio = estaura <= 1.71
print(isEstauraPromedio)
print("su estatura es",estaura)
#datos familiares 
NombreMadre = "yensy mendez"
EdadMadre = 48
NombrePadre = "pablo amaya" 
EdadPadre = 47
NombreHermano = "sneider arbelaez mendez"
EdadHermano = 28
print ("#"*15," el padre es mayor que la madre", "#"*15)
isMayorPadreQueMadre = EdadPadre > EdadMadre
print (isMayorPadreQueMadre)
print("la diferencia de edad es", EdadMadre - EdadPadre)
print ("#"*15," a que edad tuvieron su segundo hijo", "#"*15)
isEdadQueTenian = EdadPadre - edad, EdadMadre - edad
print(isEdadQueTenian)
print ("#"*15," años de diferencia de hijos", "#"*15)
isDiferenciaDeEdad = EdadHermano - edad
print(isDiferenciaDeEdad)
isMayorSneider = EdadHermano > edad
print (isMayorSneider)
print("es mayor sneider que santiago")
#algunas operaciones aunque ya hice anteriormente
print ("#"*15,"operaciones con edades", "#"*15)
print ( EdadPadre - EdadHermano)
print( EdadHermano + EdadMadre)
print( edad / EdadHermano)
isSumaEdadPdreYMadre = EdadPadre + EdadMadre
print (isSumaEdadPdreYMadre/EdadHermano)
print ("#"*15," nombre de la familia de mayor a menor", "#"*15)
print (NombreMadre, NombrePadre,NombreHermano,nombre)
#santiago amaya mendez estudiante de ingernieria biomedica universidad CES 






