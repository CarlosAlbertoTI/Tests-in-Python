def multiplicar(*lista):
	numero = 1
	for i in lista:
		numero = i * numero
	return numero


print(multiplicar(2,3,2))	
