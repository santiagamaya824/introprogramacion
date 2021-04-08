guardar  =  imprimir ( 'hola' )
print() ( guardar )

guardar  =  redondo ( 14.2534897 , 2 )
imprimir ( guardar )

def  linedesign ( cantidad  =  10 , simbolo  =  '#' ):
    imprimir ( simbolo  * cantidad )
    return None

linedesign ( 30 , '#' )
linedesign ( 10 , '*' )
linedesign ( 100 , '♦' )


# ---------- Muestre la lista ----------- #
def  mostrarLista ( listaEntrada  = []):
    for elemento  in  listaEntrada :
        imprimir ( elemento )
    return  None
lista = [ 213 , 32 , 23123 , 321 , 321 , 233 , 1232 , 23 ]
lista2  = [ 564654 , 645 , 64543 , 2565 , 547 , 57865 ]
linedesign() ( 30 , '☺' )
mostrarLista ( lista )
linedesign ( 3 , '(ง • ̀_ • ́) ง' )
mostrarLista ( lista2 )
# ---------- Sumar dos números ----------- #
def  sumar ( a  =  0 , b  =  0 ):
    suma  =  a  +  b
    return suma
linedesign() ( 30 , '♣' )
resultado =  sumar ()
imprimir ( resultado )
imprimir ( sumar ( 12 , 14 ))
redonda ( 12.234897 , 2 )
# ---------- Restar dos números ----------- #
def  restar ( a  =  0 , b  =  0 ):
    resta  =  a  -  b
    return resta
# ---------- Multiplicar dos números ----------- #
def  multiplicar ( a  =  0 , b  =  0 ):
    multiplica  =  a  *  b
    return multiplica
# ---------- dividir dos números ----------- #
def  dividir ( a  =  0 , b  =  1 ):
    dividi  =  a  /  b
    return dividi
# ---------- potenciar dos números ----------- #
def  potenciar ( base  =  0 , exponente  =  1 ):
    potencia  =  base  **  exponente
    return potencia

# ---------- funciones dependientes de otras ----------- #
def  calcular ( operacion , numeroA , numeroB ):
    print ( operacion ( numeroA , numeroB ))


baseIngresada  =  int ( input ( 'Ingrese una base entera:' ))
exponenteIngresado  =  int ( input ( 'ingrese un exponente entero:' ))

imprimir ( restar ( 83 , 87 ))
imprimir ( multiplicar ( 83 , 87 ))
imprimir ( dividir ( 83 , 87 ))
imprimir ( dividir ())
imprimir ( potenciar ( baseIngresada , exponenteIngresado ))

calcular ( sumar , 63 , 67 )