# Exercício 13
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

x = float(input('Qual é o seu salário atual? '))

aum = x * 0.15
sal = x + aum

print('O seu novo salário é R${:.2f}'.format(sal))
