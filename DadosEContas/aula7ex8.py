# Exercício 11
# Faça um programa que leia a largura e a altura de uma parede em mestros, calcule sua área e a quantidade de tinta necessária para pontá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

x = int(input('Qual altura da parede? '))
y = int(input('Qual o comprimento da parede? '))

a = x * y
t = (a // 2)

if a % 2 != 0:
    t = t + 1

print('A área da parede é {} e serão necessárias {} latas de tinta'.format(a, t))
