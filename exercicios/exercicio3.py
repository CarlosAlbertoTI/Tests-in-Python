saque = int( input('Digite quanto você quer sacar: '))
if 10 <= saque <= 600:
	#trabalhe apenas com valores de 100 em 100
	print('Notas de R$100 a serem sacadas :',saque//100)
	saque = saque - ((saque//100)*100) 

	print('Notas de R$50 a serem sacadas :',saque//50)
	saque = saque -  ((saque//50)*50) 
	
	print('Notas de R$10 a serem sacadas :',saque//10)
	saque = saque - ((saque//10)*10) 
	
	print('Notas de R$5 a serem sacadas :',saque//5)
	saque = saque - ((saque//5)*5)
	
	print('Notas de R$1 a serem sacadas :',saque//1)
else:
	print('Valores indisponiveis')

