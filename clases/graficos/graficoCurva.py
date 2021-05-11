from time import asctime


import  pandas  as  pd
import  matplotlib . pyplot  as  plt
ecgData  =  pd . read_csv ( 'ecg.csv' , codificación = 'UTF-8' , encabezado = 0 , delimitador = ';' ). to_dict ()
print ( ecgData . teclas ())
muestras  =  lista ( ecgData [ 'muestra' ]. valores ())
print ( muestras )
voltaje  =  lista ( ecgData [ 'valor' ]. valores ())
print ( voltaje [ - 10 :])
plt . parcela ( Muestras , Voltaje )
plt . mostrar ()