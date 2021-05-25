texto  =  'Hola espero que todo ande bien'
lista  = [ 1 , 434 , 53 , 2 , 2 ]
lista . ordenar ()
print( lista )
lista . pop ( 2 )
for  elemento  in  lista :
    print ( elemento )
for i  in range ( len ( lista )):
    print ( lista [ i ])

for  letra  in  texto :
    print ( letra )

print ( texto [ 1 ])
palabras  =  texto . dividir ( '' )
print ( palabras )
print ( tipo ( palabras ))
eliminarE =  texto . dividir ( 'e' )
datos  =  'nombre; apellido; edad'
print ( datos . split ( ';' ))
print ( eliminarE )

uniendo =  'yo' . unirse ( eliminarE )
print ( uniendo )
info  =  '' . unirse ( datos . split ( ';' ))
print ( info )

listaNombres  = [ 'Laura' , 'Juan' , 'Mario' , 'Elsa' , 'Katherine' , 'daniel' , 'Raúl' , '©' , '■' ]
print ( max ( listaNombres ))
print ( max ( listaNombres , key = len ))


respuesta  =  input ( 'Ingrese Si o No:' )
print ( respuesta . superior ())
if respuesta . superior () ==  'SI' :
    print ( 'Hola bienvenido al código' )
else :
    print ( 'chao !!' )

nombre  =  input ( 'Ingrese su nombre:' )
print ( nombre . capitalize ())
print (tipo ( nombre ))

correo  =  'ESPERO QUE ESTES BIEN'
print ( correo . casefold (). capitalize ())
saludo  =  'Hola como estas?'
nombre  =  'Maria Alejandra'
nombre  =  'maria alejandra'
nombres  =  nombre . dividir ( '' )
nombre =  ''
for  elemento  in  nombres :
    nombre  + =  elemento . capitalizar () + ''
print ( nombre )
print ( saludo . center ( 50 ))
print ( nombre . center ( 50 ))

enunciado  =  'Hola hola ya me cansé de decir tantos Hola pero como vamos hola'
print ( enunciado . upper (). count ( 'HOLA' ))

print ( enunciado . encontrar ( 'decir' ))
impresión (Traducción literal [ 25 : 30 ])

txt  =  'me gusta programar en java'
print ( txt . reemplazar ( 'java' , 'python' ))

numeroId  =  '123124'
print ( numeroId . isnumeric ())

parrafo  =  'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas debitis hic libero quos, aliquam nostrum officia! Unde, magnam ex? Vel aliquid ducimus aliquam error quod rem ut quos animi numquam. '

print ( parrafo . termina con ( '.' ))