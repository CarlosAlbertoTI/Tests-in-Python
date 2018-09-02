#4
#1+2+3+4
numero = int( input('Dgite um numero positivo: '))
i = 0
if numero > 0 :
	resultado = 0
	while i <= numero:
		resultado = resultado + i
		i = i + 1	
	print('A soma de 1 ate ',numero,' e = ',resultado)
else:
	print('Digite um numero maior do que zero')
