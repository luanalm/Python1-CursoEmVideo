# Exercício 30
# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar

x = int(input('Adicione um número inteiro: '))

if x%2 == 0:
    print('O número {} é par'.format(x))
else:
    print('O número {} é ímpar'.format(x))
