#Aqui explicaremos como hacer un gráfico de barras
import  matplotlib.pyplot as  plt 
lenguajes  = [ 'py' , 'java' , 'dardo' , 'ts' , 'elixir' ]
encuesta  = [ 50 , 10 , 20 , 10 , 10 ]
plt . bar ( lenguajes , encuesta , ancho  = 0.9 , color  =  'm' )
###############
#titulo
plt . title ( 'Lenguajes más usados' )
plt . xlabel ( 'Lenguajes de programación' )
plt . ylabel ( '% de uso de lenguajes' )
plt . savefig ( 'graficoLenguajes.png' )
###############
plt . mostrar ()