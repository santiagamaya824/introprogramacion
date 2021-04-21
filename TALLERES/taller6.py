#-------taller clases y objetos-----------#

class Torta():
    def __init__ (self,formaEntrada, saborEntrada, alturaEntrada):
        self.forma = formaEntrada
        self.sabor = saborEntrada
        self.altura = alturaEntrada
        print(f""" 
        mi forma es {self.forma}
        mi sabor es {self.sabor}
        mi altura es {self.altura} centimetros
        """)

print("torta numero 1")
torta1 = Torta(f"redonda","chocolate",45)
print("torta numero 2")
torta2 = Torta(f"cuadrada","vainilla",30)

class Estudiante():
    def __init__(self,edadEntrada,nombreEntrada,idEntrada,carreraEntrada,semestreEntrada):
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.id = idEntrada
        self.carrera = carreraEntrada
        self.semestre = semestreEntrada
        print(f"""
        hola mi nombre es {self.nombre}
        tengo {self.edad} años
        mi id es {self.id}
        estudio {self.carrera} en la universidad CES
        estoy en el {self.semestre} semestre
        """)
    def tiempoEstudio(self,materia,tiempo):
        print(f"voy a estudiar{materia} por {tiempo}horas")

print("estudiante 1")
estudiante = Estudiante(20, "santiago", 12345, "ingenieria biomedica", 5)
tiempo = tiempoEstudio ("programacion",20)

class Nutricionista():
    def __init__(self,edadEntrada,nombreEntrada,universidadEntrada):
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.universidad = universidadEntrada
        self.estatura = Estatura
        self.peso = Peso
        self.imc = Peso/(Estatura**2)
        print(f"""
        hola mi nombre es {self.nombre}
        tengo {self.edad} años
        soy nutricionista egresado de la universidad {self.universidad} 
        voy a calcular tu imc, porfavor responde las siguientes preguntas
        """)

print("nutricionista")
Nutricionista(28, "juan", "CES")

class Canguro():
    def __init__(self,edadEntrada,idEntrada,nombreEntrada):
        self.edad = edadEntrada
        self.id = idEntrada
        self.nombre = nombreEntrada
    def saltos (self,numerodesaltos):
        for elemento in range(saltos):
            print (f"soy un canguro y he dado",{elemento + 1})

salto = saltos(3)
