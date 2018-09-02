numero = int( input('Digite um numero: '))
n = 1
j = 2
k = 3

while n + j + k <= numero:
	teste = n + j + k 
	if  teste is numero:
		print('o numero %i e perfeito' %(numero))
	if teste < numero-1 or teste > numero:
		print('O numero %i não e perfeito' %(numero))
	n = n + 1
	j = j + 1
	k = k + 1

		

	
