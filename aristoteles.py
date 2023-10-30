def monitoreoViajeEnElTiempo(n:int):
	##n = 2023 #es el parámetro y valor inicial, por eso está mal. Tiene que poder ser modificado
	while n > (-384): ##la especificación pide lo más cercano al -384
		  print(n) ## estaba mal el orden, esta función imprime el lugar de partida
		  n = n - 20
		  

print(monitoreoViajeEnElTiempo(2023))

def delUnoAlDiez():# se usan los paréntesis solos cuando no recibe un parámetro(¿Argumento?)
	contador = 0 ##
	while contador<10:
		print(contador)
		contador=contador+1 ##va sumando, otra forma "contador+=1"

print(delUnoAlDiez())

def numeros_10_al_40():
    i=10
    while (i<=40):
        print(i)
        i+=2 ##es así la sintaxis de Python, es equivalente a i = i+2

print(numeros_10_al_40())
