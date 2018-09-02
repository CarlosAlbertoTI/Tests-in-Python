n = int( input('Digite a quantidade de termos: '))
j = int( input('Escolha um numero para realizar ass operações: '))
k = int( input('Escolha um segundo numero para realizar as operações: '))
lista = []
for i in range(n+1):
	if ( i%j==0 or i%k==0) or (i%j==0 and i%k==0):
		lista.append(i)
print(lista)	 	

