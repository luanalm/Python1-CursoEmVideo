# Exercício 10
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00 = R$3,27

x = int(input('Quanto dinheiro você tem na carteira? R$'))

dol = x / 3.27

print('Com esse dinheiro você consegue comprar {:.2f} dolares americanos'.format(dol))
