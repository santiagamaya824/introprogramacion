import funciones  as fn
import  aleatoriamente  as  rd
def  sumar ( a , b ):
    return  a + b
imprimir ( sumar ( 2 , 6 ))
imprimir ( fn . sumar ( 2 , 4 ))
imprimir ( fn . calcular ( sumar , 2 , 4 ))
imprimir ( fn . calcular ( fn . sumar , 2 , 4 ))

imprimir ( rd . randint ( 2 , 6 ))