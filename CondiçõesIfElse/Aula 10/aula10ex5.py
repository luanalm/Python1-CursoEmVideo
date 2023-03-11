# Exercício 32
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

print('Descubra se um ano foi ou será bissexto.')
ano = int(input('Digite o ano: '))

if ano < 2023:
    if ano % 4 == 0:
        print('O ano {} foi um ano bissexto!'.format(ano))
    else:
        print('O ano {} não foi um bissexto!'.format(ano))
else:
    if ano % 4 == 0:
        print('O ano {} será um ano bissexto!'.format(ano))
    else:
        print('O ano {} não será um ano bissexto!'.format(ano))
