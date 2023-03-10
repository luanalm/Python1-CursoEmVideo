# Exercício 28
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num = random.randint(0, 5)
nuser = int(input('De 0 a 5, qual número você acha que foi sorteado: '))

if num == nuser:
    print('O número sorteado foi {}. Parabens! Você acertou!'.format(num))
else :
    print('Ah que pena! Você errou. Você advinhou o número {} e número sorteado foi {}'.format(nuser, num))
