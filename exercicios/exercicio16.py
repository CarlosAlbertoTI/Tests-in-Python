import random

contador = int( input('Digite quantos testes você deseja fazer: '))
cont = 0

for i in range(contador):

	#gerando as listas vazias
	mega_sort = []
	num_sort_jogador = []

	#pegando numeros com random e colocando em mega_sort
	while len(mega_sort) < 6:
		numero = random.randrange(1,61)
		if mega_sort.count(numero) < 1 :
			mega_sort.append(numero)
	#colocando os valores em ordem		
	mega_sort.sort()	

	#print('Numero para sorteio: ',mega_sort)	

	while num_sort_jogador != mega_sort:
		num_sort_jogador = []
	#pegando os numeros de sorteio do jogador
		while len(num_sort_jogador) < 6:
			numero_jogador = random.randrange(1,61)
			if num_sort_jogador.count(numeroj_ogador) < 1:
				num_sort_jogador.append(numero_jogador)		
		#colocando os valores em ordem
		num_sort_jogador.sort()
	
		#print('Numero do jogador: ',num_sort_jogador)		
		cont+=1	

	print('Parabens!!, você conseguiu acertar os numeros do sorteio!!')
	print('Quantidade de tentativas: ',cont)	