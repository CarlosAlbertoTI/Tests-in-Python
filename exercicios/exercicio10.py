n = int( input('Digite o numero de contagem: '))
j = int( input('Digite o primeiro numero de comparação: '))
k = int( input('Digite o segundo numero de comparação: '))
lista = []
for i in range(n+1):
	if i > 1:
		if i%j==0 and i%k==0:
			lista.append(i)
print(lista)		 
