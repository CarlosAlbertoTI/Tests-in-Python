import random

mega_sena = []
jogador = []
mega_sorte = list(range(1,61))
mega_sorte2.copy(mega_sorte)

num = int(input('Quantas vezes você deseja testar: '))
cont = 0
ganhou = True

#cria os valores padrões para testar
for i in range(1,7):
		aleatorio =  random.choice(mega_sorte)
		mega_sena.append(aleatorio)
		mega_sorte.remove(aleatorio)

mega_sena.sort()
"""
agora o loop vai criar o jogo do apostador e verificar com o cartão resposta
para depois verificar se se ele acertou uma quarta, quinta ou se tiver sorte um jogo
inteiro contando quantas vezes ele precisou jogar

"""
while 1:
	jogador = []
	#primeiro vamos incrementar os numeros do apostador
	for k in range(1,7):
		aleatorio =  random.choice(mega_sorte2)
		jogador.append(aleatorio)
		mega_sorte2.remove(aleatorio)

	for l in len(jogador):
		if mega_sena[l] == jogador[l]:
			cont+=1
	
	if cont == 6:
		print('Parabens, você ganhou a TeleSena, você é um milhonário')
		print('Numero de tentativas: ', cont)
		break;		

	elif cont == 4:
		print('Parabens!! Você ganhou um quarta!')
		print('Quantidade de tentativas: ',cont)
		break;
	elif cont == 5:
		print('Parabens!! Você ganhou um quinta!')
		print('Quantidade de tentativas: ',cont)
		break;



