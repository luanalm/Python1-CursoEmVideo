# Exercício 17
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import hypot

x = float(input('Tamanho do cateto oposto: '))
y = float(input('Tamanho do cateto adjacente: '))

print('O tamanho da hipotenusa desse triângulo é {:.2f}'.format(hypot(x,y)))
