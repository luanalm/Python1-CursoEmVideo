# Exercício 12
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

x = float(input('Preço atual do produto: '))

des = x * 0.05
val = x - des

print('O valor do produto com o desconto fica R${:.2f}'.format(val))
