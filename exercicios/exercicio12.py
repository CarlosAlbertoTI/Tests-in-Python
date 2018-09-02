lista = []
i = 1
print('Enquete: Quem foi o melhor jogador?')
print('\n')
print('Informe um valor entre 1 e 23 ou 0 para sair!')
while i == 1:
	jogador = int( input('Número do jogador (0 = fim) :  '))
	if jogador == 0:
		print('para')
		i = 0
	elif 0 < jogador < 24:
		lista.append(jogador)

print('Resultado da votação:')
print(' \n \n ')
print(' Foram computados '+str(len(lista))+' votos')

print('jogador               votos                 %')
for j in range(len(lista)):
	cont = lista.count(lista[j])
	porcentagem = ( lista.count(lista[j])/len(lista) ) *100 
	if lista[:j].count(lista[j]) < 1:
		print (lista[j],'                    ',cont,'                ',porcentagem,'%')
