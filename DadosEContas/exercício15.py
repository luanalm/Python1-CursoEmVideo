# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantidade de quilometros percorridos: '))
qd = int(input('Por quantos dias o carro foi alugado: '))

val1 = 0.15 * km
val2 = 60 * qd

valt = val1 + val2

print('O valor a ser pago pelo aluguel desse carro é R${:.2f}'.format(valt))