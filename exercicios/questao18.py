def preco_imposto(preco, percent):
	novo_preco = preco + ((percent/100)*preco)
	return novo_preco

imposto = float( input('Digite a taxa de imposto [%]:  '))
preco_prod = float( input('Digite o preço do produto sem imposto: '))

print(preco_imposto(preco_prod,imposto))
