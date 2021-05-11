# quiz 3 santiago amaya mendez
import matplotlib.pyplot as plt
import pandas as pd 

snack1 = input ("ingresa tu snack preferido : ")
precio1 = int(input("ingresa el precio del snack : "))
snack2 = input ("ingresa tu snack preferido : ")
precio2 = int(input("ingresa el precio del snack : "))
snack3 = input ("ingresa tu snack preferido : ")
precio3 = int(input("ingresa el precio del snack : "))
snack4 = input ("ingresa tu snack preferido : ")
precio4 = int(input("ingresa el precio del snack : "))
snack5 = input ("ingresa tu snack preferido : ")
precio5 = int(input("ingresa el precio del snack : "))

listaSnacks = [snack1, snack2, snack3, snack4, snack5]
listaPrecio = [precio1, precio2, precio3, precio4, precio5]

plt.bar(listaSnacks,listaPrecio)
plt.xlabel("snacks")
plt.ylabel("precio")
plt.title("grafico barras")
plt.savefig ("barras.png")
plt.show()

ciudad1 = input ("ingresa tu ciudad preferida : ")
poblacion1 = input ("ingresa la poblacion de la ciudad : ")
ciudad2 = input ("ingresa tu ciudad preferida : ")
poblacion2 = input ("ingresa la poblacion de la ciudad : ")
ciudad3 = input ("ingresa tu ciudad preferida : ")
poblacion3 = input ("ingresa la poblacion de la ciudad : ")
ciudad4 = input ("ingresa tu ciudad preferida : ")
poblacion4 = input ("ingresa la poblacion de la ciudad : ")
ciudad5 = input ("ingresa tu ciudad preferida : ")
poblacion5 = input ("ingresa la poblacion de la ciudad : ")

listaCiudades = [ciudad1, ciudad2, ciudad3, ciudad4, ciudad5]
listaPoblacion = [poblacion1, poblacion2, poblacion3, poblacion4, poblacion5]
explode = [0,0,0,0,0]

maximo = max(listaPoblacion)
ubicacion = listaPoblacion.index(maximo)
explode[ubicacion] = 0.1

plt.pie(listaPoblacion,explode,labels=listaCiudades)
plt.title("grafica torta")
plt.savefig ("torta.png")
plt.show()

print("definicion ecg : el elecetrocardiograma es una representacion de la actividad electrica que ejerce el corazon en funcion del tiempo,Cada vez que el corazón late, una señal eléctrica circula a través de él, Un electrocardiograma muestra si su corazón está latiendo a un ritmo y con una fuerza normal. ")
print("definicion ppg : el fotopletismograma es una técnica de pletismografía en la cual se utiliza un haz de luz para determinar el volumen de un órgano, Una fuente de luz infrarroja emite un haz sobre la piel para iluminar los vasos subcutáneos, estos reflejan parte de dicho haz dependiendo la cantidad de hematíes que contienen. ")

df = pd.read_csv("ecg.csv",sep = ";")
valor_ecg = df["valor"]

plt.plot(valor_ecg)
plt.title("grafica ECG")
plt.xlabel("tiempo")
plt.ylabel("mV")
plt.savefig("ecg.png")
plt.show()

df2 = pd.read_csv("ppg.csv", sep = ";")
valor_ppg = df2["valor"]

plt.plot(valor_ppg)
plt.title("grafica PPG")
plt.xlabel("tiempo")
plt.ylabel("volumen")
plt.savefig("ppg.png")
plt.show()

