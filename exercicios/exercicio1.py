metros = int( input('Quantos metros quadrados de área você quer que seja pintada: '))
#Isso diz quantos litros ele precisa para pintar 
litros_tinta = metros//3
if metros % 3 > 0:
	litros_tinta = litros_tinta + 1
#print(litros_tinta)
#calcule quantas latas ele precisa
quant_latas  = litros_tinta//18
if litros_tinta % 18 > 0:
	quant_latas = quant_latas + 1
#print(quant_latas)
#calcule o quanto que ele vai pagar sabendo que uma lata custa R$80,00
preco_latas = quant_latas * 80
#informe ao usuário quantas latas sera necessario comprar e quanto ele devera gastar
print('Qunatidade de litros necessarios: ',litros_tinta)
print('Quantidade de latas necessarias: ',quant_latas)
print('O preço pelas latas necessarias: R$',preco_latas)

