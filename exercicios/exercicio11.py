salario = float( input('Digite o seu salario: R$'))
if salario <= 0:
	print('Salario invalido')
else:
	if 0 < salario <= 280.00:
		print('Salario inicial: R$ %.2f' %salario)
		print('O percentual de aumento aplicado: 20%')		
		print('Valor do aumento: R$ %.2f' %( (20/100)*salario ))
		print('Novo Salario: R$ %.2f' %( salario + ((20/100)*salario)  ))
	elif 280.00 < salario <=700.00:
		print('Salario inicial: R$ %.2f' %salario)
		print('O percentual de aumento aplicado: 15%')		
		print('Valor do aumento: R$ %.2f' %( (15/100)*salario) )
		print('Novo Salario: R$ %.2f' %( salario + ((15/100)*salario)  ))
	elif 700.00 < salario <= 1500.00:
		print('Salario inicial: R$ %.2f' %salario)
		print('O percentual de aumento aplicado: 10%')		
		print('Valor do aumento: R$ %.2f' %( (10/100)*salario) )
		print('Novo Salario: R$ %.2f' %( salario + ((10/100)*salario)  ))	
	else:
		print('Salario inicial: R$ %.2f' %salario)
		print('O percentual de aumento aplicado: 5%')		
		print('Valor do aumento: R$ %.2f' %( (5/100)*salario) )
		print('Novo Salario: R$ %.2f' %( salario + ((5/100)*salario)  ))
	
