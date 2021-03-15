# ---- Preguntas
preguntaNumero  =  '' 'Ingrese alguna de estas opciones
    1.Hacer conversión de pesos a dólares o euros
    2.Agrege un valor a la lista de pesos
    3.Mostrar valor más alto, más bajo y promedio
    4.Eliminar elemento de la lista
    5. Salir
'' '
preguntaMoneda  =  '' '
    C- Mostrar original en pesos colombiano
    D- Mostrar en Dolares
    E- Mostrar en Euros
'' '
preguntarNumero  =  'Ingrese un valor en COP:'
preguntaBorrarCoordenada  =  'Ingrese la posición que desea borrar:'
# ---- Mensajes --- #
mensajePesos  =  'Mostrando lista original'
mensajeDolares  =  'Mostran Lista en dolares'
mensajeEuros  =  'Mostran Lista en euros'
mensajeMayor  =  'El mayor numero ingresado es ->'
mensajeMenor  =  'El menor numero ingresado es ->'
mensajePromedio  =  'El promedio es ->'
mensajeDespedida  = '☺Que tengas un feliz día ☺☻'
#----Error---#
mensajeErrorEntrada  = 'valor ingresado no valido'


listaPesos  = [ 20000 , 30000 , 4000 , 2500 , 1000 , 7600 ]

# Conversión punto 1
listaEuros  = []
for  elemento  in listaPesos :
    conversor  =  ronda ( elemento * 0.00023 , 2 )
    listaEuros . append ( conversor )
listaDolares  = []
for  elemento  in  listaPesos :
    conversor  =  ronda ( elemento * 0.00028 , 2 )
    listaDolares . append ( conversor )


opcionEscogida  =  int ( input ( preguntaNumero ))
while ( opcionEscogida  ! = 5 ):
    # --------- Opcion1 --------- #
    if ( opcionEscogida  ==  1 ):
        opcionMoneda  =  entrada ( preguntaMoneda )
        if ( opcionMoneda  ==  'C' ):
            imprimir ( mensajePesos )
            imprimir ( listaPesos )
        elif ( opcionMoneda  ==  'D' ):
            imprimir ( mensajeDolares )
            imprimir ( listaDolares )
        elif ( opcionMoneda  ==  'E' ):
            imprimir ( mensajeEuros )
            imprimir ( listaEuros )
        otra cosa :
            imprimir ( mensajeErrorEntrada )
    # --------- Opcion2 --------- #
    elif ( opcionEscogida  ==  2 ):
        valorIngresado  =  float ( input ( preguntarNumero ))
        listaPesos . añadir ( valorIngresado )
        imprimir ( listaPesos )
    # --------- Opcion3 --------- #
    elif ( opcionEscogida  ==  3 ):
        imprimir ( mensajeMayor , max ( listaPesos ))
        imprimir ( mensajeMenor , min ( listaPesos ))
        imprimir ( mensajePromedio , sum ( listaPesos ) / len ( listaPesos ))
    # --------- Opcion4 --------- #
    elif ( opcionEscogida  ==  4 ):
        imprimir ( listaPesos )
        posicion  =  int ( input ( preguntaBorrarCoordenada )) -  1
        listaPesos . pop ( posicion )
        imprimir ( listaPesos )
    # --------- Opcion no valida --------- #
    else :
        imprimir ( mensajeErrorEntrada )
    opcionEscogida  =  int ( input ( preguntaNumero ))

imprimir ( mensajeDespedida )