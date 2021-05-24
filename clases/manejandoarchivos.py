import  sys
nombre   =  input ( 'ingrese su nombre:' )
edad  =  int ( input ( 'ingrese su edad:' ))
estatura  =  float ( input ( 'ingrese su estatura:' ))

nombreArchivo  =  "estudiantes.txt"
try :
    archivo  =  open ( nombreArchivo )
    print ( '1' )
except  FileNotFoundError :
    archivo  =  open ( nombreArchivo , 'w' , encoding = 'UTF-8' )
    descripcion  =  'Archivo de datos de estudiantes'
    print ( "2" )
    archivo . Writelines ( descripcion )
    sys . exit ( 1 )

archivo  =  open ( nombreArchivo, "a")
linea  =  " \ n nombre:"  +  nombre  +  "edad:" +  str ( edad ) +  "estatura:" +  str ( estatura )
archivo.Writelines ( linea )
archivo.close ()

#mirada lasciva
with  open ( nombreArchivo , 'r' ) as  lector :
    for línea  in lector :
        print ( línea )