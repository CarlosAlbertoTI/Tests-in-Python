metros = int( input('Quantos metros quadrados de área você quer que seja pintada: '))
#Isso diz quantos litros ele precisa para pintar 
litros_tinta = metros//6
if metros % 6 > 0:
	litros_tinta = litros_tinta + 1

#calcule galões latas de 18L precisa
quant_galoes  = litros_tinta//18
if litros_tinta % 18 > 0:
	quant_galoes = quant_galoes + 1

#calcule quantas latas de 4L precisa
quant_latas = litros_tinta//4
if litros_tinta % 4 > 0:
	quant_latas = quant_latas + 1

#calcule o quanto que ele vai pagar sabendo que uma galao custa R$80,00
preco_galao = quant_galoes * 80
#calcule o quanto que ele vai pagar sabendo que uma lata custa R$25,00
preco_lata = quant_latas * 25
#informe ao usuário quantas latas sera necessario comprar e quanto ele devera gastar
print('Qunatidade de litros necessarios: ',litros_tinta,'litros')
print('Quantidade de galoes necessarios: ',quant_galoes)
print('Quantidade de latas necessarias: ',quant_latas)
print('O preço pelas galoes necessarias: R$',preco_galao)
print('O preço pelas latas necessarias: R$',preco_lata)
