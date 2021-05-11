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
        print(f"voy a estudiar{materia} por {tiempo} horas")

print("estudiante 1")
estudiante = Estudiante(20, "santiago", 12345, "ingenieria biomedica", 5)
estudiante.tiempoEstudio("calculo", 20) 

class Nutricionista():
    def __init__(self,edadEntrada,nombreEntrada,universidadEntrada):
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.universidad = universidadEntrada
        print(f"""
        hola mi nombre es {self.nombre}
        tengo {self.edad} años
        soy nutricionista egresado de la universidad {self.universidad} 
        voy a calcular tu imc, porfavor responde las siguientes preguntas
        """)
    def IMC (self,peso,estatura):
        print(f"hola soy {self.nombre} y voy a medir el imc")
        imc = peso/(altura**2)


print("nutricionista")
nutricionista = Nutricionista(28, "juan", "CES")
nutricionista.IMC(68, 1.72)

class Canguro():
    def __init__(self,edadEntrada,idEntrada,nombreEntrada):
        self.edad = edadEntrada
        self.id = idEntrada
        self.nombre = nombreEntrada
    def saltos (self,numerodesaltos):
        for elemento in range(salto):
            print (f"""hola soy un canguro, me llamo {self.nombre} 
            mi id es {self.id} tengo {self.edad} años 
            y he dado {elemento + 1} saltos""")

print("canguro")
canguro = Canguro(20,123456,"victor")
canguro.salto (6)

