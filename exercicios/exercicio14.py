lista = []
i = 0
cont = 0
while i == 0:
	numero = int( input('Digite um número para a lista: '))
	if numero == -1:
		i = 1
	else:
		lista.append(numero)

for i in range(len(lista)):
	if lista[i]%2 == 0:
		print(lista[i])


