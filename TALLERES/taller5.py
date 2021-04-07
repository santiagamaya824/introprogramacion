#-------taller 5 funciones-----#

listaPesos = [1,2,3,4,5,6,7,8,9,15,20,30,40,50,77,85,95,100]

print("#"*20, " numeros de la lista ", "#"*20)
#--------punto 1---------#
def lista ():
    for elemeto in listaPesos:
        print(elemeto)

lista()

#--------punto 2---------#
def pesos ():
    print( "este es el mayor de la lista : " , max ( listaPesos ))
    print("este es el menor de la lista : " , min ( listaPesos ))
    print("este es el promedio de lista : " , sum ( listaPesos ) / len ( listaPesos))

pesos()

print("#"*20, " saludos ", "#"*20)
#--------punto 3--------#
def saludo (veces):
    for saludo in range (veces):
        print("buenos dias mi bebe")

veces = int(input("ingrese numero de saludos : "))

saludo(veces)

print("#"*20, " numeros pares de la lista ", "#"*20)
#---------punto 4----------#
def numerosPares ():
    for numeros in listaPesos:
        if (numeros%2 == 0):
            print(numeros)

numerosPares()

print("#"*20, " numeros mayores a 24 ", "#"*20)
#---------punto 5-----------#
def numeroMayores():
    for mayores in listaPesos:
        if (mayores > 24):
            print(mayores)

numeroMayores()

print("#"*20, " tu imc ", "#"*20)
#---------punto 6-----------#
def IMC (peso,estatura):
    imc = peso/(estatura**2)
    return imc

peso = float(input("ingrese su peso : "))
estatura = float(input("ingrese su estaura : "))

tu_imc = IMC(peso, estatura)
print("su imc es : ", tu_imc)

print("#"*20, " despedida ", "#"*20)
#---------punto 7-----------#
def despedida (nombre):
    print("que tengas un lindo dia ", nombre)

nombre = input("cual es tu nombre : ")

despedida(nombre)

# santiago amaya mendez 





