# Exercício 18
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

x = float(input('O valor de um ângulo: '))

print('O ângulo {:.2f}, possui o seno {:.2f}, o cosseno {:.2f} e a tangente {:.2f}'.format(x, math.sin(x), math.cos(x), math.tan(x)))
