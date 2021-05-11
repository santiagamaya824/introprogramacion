#------------taller herencias-------#

class Persona():
    def __init__(self,idEntrada,nombreEntrada,edadEntrada):
        self.id = idEntrada
        self.nombre = nombreEntrada
        self.edad = edadEntrada
    def hablar (self,mensaje):
        print("mi nombre es {self.nombre} tengo {self.edad} años. identificados con id numero {self.id} y tengo algo por decir....",mensaje)

class Caminar():
    def __init__(self,cantidadPasos):
        print({cantidadPasos})

personita = Persona(12345678, "alberto", 43)
personita.hablar("bienbenidos al codigo")
personita.cantidadPasos(10)