# Exercício 18
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

ang = float(input('O valor de um ângulo: '))

s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))

print('O ângulo {:.2f}, possui o seno {:.2f}, o cosseno {:.2f} e a tangente {:.2f}'.format(ang, s, c, t))
