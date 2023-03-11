# Exercício 31
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

dist = float(input('Distância da viagem em quilometros: '))

if dist < 200:
    val = dist * 0.50
    print('O preço da passagem para essa viagem será: R${:.2f}.'.format(val))
else:
    val = dist * 0.45
    print('O preço da passagem para essa viagem será: R${:.2f}.'.format(val))
