numero = int( input('Digite um numero positivo: '))
if numero > 0:
	i = 0
	while i <= numero:
		if i%3 is 0:
			print(i)		
		i = i + 1
else:
	print('Digite um numero maior do que zero')
