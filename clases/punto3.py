repeticionCiclos = 1

while (repeticionCiclos == 1):
    try:
        nombre = str(input("ingresa tu nombre: "))
        assert (nombre.isalpha())
        repeticionCiclos = 2
    except AssertionError:
        print ("ingresaste un dato invalido, compruebe nuevamente")

while (repeticionCiclos == 2):
    try:
        dinero_dolares = int(input("cuanto dinero tienes en dolares : "))
        repciclos = 5
    except ValueError:
        print ("dato invalido, compruebe nuevamente")

print(f"mi nombre es : " [nombre], "y tengo : " [dinero_dolares], "dolares" )