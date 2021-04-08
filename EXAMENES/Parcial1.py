#--------parcial 1 santiago amaya mendez-----------#

print("#"*20, " suma, resta, multiplicacion, divicion, potenciacion con 3 numeros ", "#"*20)

#-------punto 1--------#
# ---------- Sumar tres números ----------- #
def  sumar ( a  =  0, b  =  0,  c = 0 ):
    suma  =  a  +  b + c
    return suma
# ---------- Restar tres números ----------- #
def  restar ( a  =  0 , b  =  0, c = 0 ):
    resta  =  a  -  b - c
    return  resta
# ---------- Multiplicar tres números ----------- #
def  multiplicar ( a  =  0 , b  =  0, c = 0 ):
    multiplica  =  a  *  b * c
    return  multiplica
# ---------- dividir tres números ----------- #
def  dividir ( a  =  0 , b  =  1, c = 1 ):
    dividi  =  a  /  b
    return dividi
# ---------- potenciar tres números ----------- #
def  potenciar ( a =  0 , b  =  1, c = 1 ):
    potencia  =  a  **  b
    return  potencia

def operaciones (operacion, a, b, c):
    print(operacion(a,b,c))

operaciones(sumar, 2, 3, 4)
operaciones(restar, 2, 1, 4)
operaciones(multiplicar, 2, 3, 4)
operaciones(dividir, 2, 3, 4)
operaciones(potenciar, 2, 3, 4)

print("#"*20, " lista1 ", "#"*20)
#------punto 2--------#
listaNumero = [1,2,3,4,5,]
listaNumero2 = [10,20,30,40,50]
listaNumero3 = [100,200,300,400,500]

def lista1 ():
    for elemeto in listaNumero:
        print(elemeto)

lista1()

print("#"*20, " lista 2 ", "#"*20)

def lista2 ():
    for elemeto in listaNumero2:
        print(elemeto)

lista2()

print("#"*20, " lista 3 ", "#"*20)

def lista3 ():
    for elemeto in listaNumero3:
        print(elemeto)

lista3()

print("#"*20, " area triangulo ", "#"*20)
#------punto 3-------#
def area (base, altura):
    area = (base * altura)/2
    return area

base = float(input("ingrese su base : "))
altura = float(input("ingrese su altura : "))

tu_area = area (base, altura )
print("su area es : ", tu_area)

#------punto 4-------#
def lista ():
    print( "este es el mayor de la lista : " , max ( listaNumero ))
    print("este es el menor de la lista : " , min ( listaNumero ))
    print("este es el promedio de lista : " , sum ( listaNumero ) / len ( listaNumero))

lista()

print("#"*20, " fibonacci ", "#"*20)
#-------punto 5------#

listaFibonacci = [0,1,1,2,3,5,8,13,21,34,55,89,144]

def listaFibo (valor):
    valor1 = 0
    valor2 = 1
    for elemento in range(valor - 1):
        secuencia = valor1 + valor2
        valor1 = valor2
        valor2 = secuencia
    return (valor1)

posicion = listaFibo(57)
print (posicion)

#------punto 6--------#
import funciones as funcionsitas





