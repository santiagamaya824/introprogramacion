while True:
    _peso = input("Ingrese su peso: ")
    
    try:
        _peso = float(_peso)
    except ValueError:
        print("El valor ingresado no es valido")
        continue

    _altura = input("Ingrese su altura: ")

    try:
        _altura = float(_altura)
    except ValueError:
        print("El valor ingresado no es valido")
        continue

    _nombre = input("Ingrese su nombre: ")

    try:
        _nombre = str(_nombre)
    except ValueError:
        print("El valor ingresado no es valido")
        continue

    imc = _peso / (_altura ** 2)
    print(imc)

    break

while True:
    _parrafo = input("Ingrese un parrafo: ")
    
    if (_parrafo[-1] != "."):
        print("No termina en punto")
        continue

    _parrafo = _parrafo.split(" ")
    
    palabra_mas_grande = max(_parrafo, key=len)
    palabra_mas_pequeña = min(_parrafo, key=len)
    
    print("palabra mas grande:", palabra_mas_grande)
    print("palabra mas pequeña:", palabra_mas_pequeña)

    break

with open("mantenimientos.txt", "a") as archivo:
    _nombre_del_equipo = input("Ingrese el nombre del equipo: ")
    _descripcion_del_equipo = input("Ingrese la descripcion: ")
    _precio_del_equipo = input("Ingrese el precio: ")

    archivo.write(_nombre_del_equipo + "," + _descripcion_del_equipo + "," + _precio_del_equipo + "\n")