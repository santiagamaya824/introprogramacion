class Humano ():
    """
        Esta es la clase Humano exige atributos
        nombreEntrada: Hace referencia al nombre del usuario
        edadEntrada: Hace referencia al edad del usuario
        estaturaEntrada: Hace referencia al estatura del usuario
        Tiene las siguientes acciones:
        * hablar (mensaje):
            dado un mensaje lo muestra en pantalla
        
        * mostrarAtributos ()
            muestra los atributos del usuario
    """
    def  __init__ ( self , nombreEntrada , edadEntrada , estaturaEntrada ):
        print ( 'Hola soy un humano nuevo' )
        self . edad  =  edadEntrada
        self . raza  =  'Humano'
        self . nombre  =  nombreEntrada
        self . estatura  =  estaturaEntrada
        self . dinero  =  0
    
    def  hablar ( self , mensaje ):
        '' 'Expresa mensaje ingesado' ''
        print ( f'Hola soy { self.nombre } tengo un mensaje que decir ... ' , mensaje )
    
    def  mostrarAtributos ( self ):
        print ( f""" Mi nombre es {self . nombre}
                    Mi estatura es {self . estatura} metros
                    Mi edad es {self . edad} años
                    Tengo ahorrado {self . dinero} peso
            """ )

    def  recorrerDistancia ( self , distanciaMetros ):
        for  elemento in rango ( distanciaMetros ):
            print ( f'Hola soy { self . nombre } y he recorrido { i + 1 } metros ' )

    def  ahorraDinero ( yo ):
        preguntaIngresarMontos  =  'Ingrese S -> para continuar añadiendo montos y N -> para finalizar:'
        preguntaMonto  =  '¿Cuánto vas a ingresar ?:'
        ingresarMontos  = entrada ( preguntaIngresarMontos )
        while ( ingresarMontos  !=  'N' ):
            monto  =  float ( input ( preguntaMonto ))
            self . dinero  =  self . dinero  +  monto
            print ( f'Soy { self . nombre } y tengo { self . dinero } pesos ' )
            ingresarMontos  = entrada ( preguntaIngresarMontos )
        return self . dinero


class  Ingeniero ( Humano ):
    def  __init__ ( self , nombreEntrada , edadEntrada , estaturaEntrada , areaEntrada ):
        Humano . __init__ ( self , nombreEntrada , edadEntrada , estaturaEntrada )
        self . area  =  areaEntrada

    def  solucionarProblemas ( self , problem ):
        print ( f'Hola soy un ingeniero y me llamo { self . nombre } y procedo a solucionar el problema { problema } ' )

class  Programador ( Humano ):
    def  crearAlgoritmo ( self , algoritmo ):
        print ( f'Hola soy { self . nombre } y procedo a resolver el algoritmo { algoritmo } ' )

class  Biomédico ( Ingeniero , Programador ):
    def  mantenimientoEquiposMedicos ( self , nombreEquipo ):
        print ( f'Hola soy { self . nombre } y procedo a arreglar el { nombreEquipo } ' )
    

class  Abogado ( Humano ):
    def  levantarAccionDeTutela ( self , nombreCliente ):
        print ( f'Hola soy { self . nombre } y estoy representando a { nombreCliente } ' )