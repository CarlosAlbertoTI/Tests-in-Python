lista = []
i = 1
palavra = ''
soma = 0
media = 0
while i == 1:
	numero = int( input('Digite um numero: '))
	if numero == -1:
		i = 0
	else:
		lista.append(numero)

#mostrar a quantidade de valores que foram lidos
print('Quantidade de valores que foram lidos : ',len(lista))
#Exibir todos os valores em ordem em que foram informados um ao lado do outro
for i in range(len(lista)):
	palavra = palavra +'|'+ str(lista[i])
	soma += lista[i]
print(palavra)
#exiba todos os valores na ordem inversa á que foram informados um abaixo do outro
for j in range(len(lista)):
	lista2 = lista[::-1]
	print(lista2[j])
	
#calcule e mostre a soma dos valores
print('A soma dos valores: ',soma)
#calcule e mostre a media dos valores	 
media = soma/ (len(lista))
print('A media dos valores: ',media)
#calcule e mostre a  quantidade de valores acima de sete
cont = 0
for i in range(len(lista)):
	if lista[i] < media:
		cont +=1
print('a  quantidade de valores abaixo de sete: ',cont)
#encerre o programa com uma mensagem
print('Mude, mude, mas começe devagar.Por que a direção é mais importante que a velocidade')
	
