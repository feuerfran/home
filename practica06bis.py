import math #en la libreria de match viene cargado p, practica 7 lunes 2 de octubre

def imprimir_hola_mundo(): 
	print("Hola Mundo") #no tiene return

def imprimir_chau_mundo():
	print("Chau mundo")

#ejercicio 5. 

def perimetro() -> float:
	return 2 * math.pi #return devuelve el resultado

def es_multiplo_de (n: int, m: int) -> bool: #separo los parametros con comas
	return	n % m  == 0 # % es mod en Python



#invoco la funcion

def es_userName_largo(s:str) -> bool:
	return len (s) >=  3 and len(s) <= 8 

 #invocación de función las invocaciones de funcionaes las vamos a agrupar abajo, ver practica6
 #invocación de función

def devolver_el_doble_si_es_par(n:int)-> int:
	if es_multiplo_de(n,2): #este es un caso, pero hay que agregar caso impar
		return 2 * n #cuendo el if se cumple devuelve esta linea
	return n #la identacion es fundamental en este caso

#def imprime_pares_10_40_(): #ahora un for en lugar del while
##	n: int = 10
##	while n <= 40:
##		print(n) #en algun lugar tiene que ser false, porque sino se cuelga. El cuerpo es lo que esta adentro del while
##		n = n + 1
##imprime_pares_10_40_()

#def imprime_pares_10_40_for(): #ahora un for en lugar del while
#	for n in range (10, 42,2):
#		print(n) #en algun lugar tiene que ser false, porque sino se cuelga. El cuerpo es lo que esta adentro del while


def cuenta_Regresiva_for(n: int):
	for i in range(0,n,-1): #antes de un tab a la derecha va :
		print(n-i)
	print("Despegue")



def cuenta_Regresiva_for2(n: int): #el scope, donde la variable esta viva
	for i in range (0,n,-1):
		print(i)

def umbertoE(): #imprimir y devolver son cosas distintas
	n : int = 0 #se usa una variable local. Vive dentro del contexto o scope
	while n < 10:
		n = n + 1
		print("Eco")

def monitoreoViajeEnElTiempo(n:int):
	##n = 2023 #es el parámetro y valor inicial, por eso está mal. Tiene que poder ser modificado
	while n > (-384):
		  n = n - 20 ##está mal el orden, el print debería ir antes
		  print(n)



print(es_multiplo_de(11,5))
print(perimetro())
print (es_userName_largo("meo"))
print(es_userName_largo("meoElHumedecido"))
cuenta_Regresiva_for(4)
cuenta_Regresiva_for2(4)
print(devolver_el_doble_si_es_par(1789))
print(devolver_el_doble_si_es_par(1878))
print(umbertoE())
print(monitoreoViajeEnElTiempo(2023))