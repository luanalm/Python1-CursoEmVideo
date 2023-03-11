# Exercício 34
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. E para os inferiores ou iguais um aumento de 15%

print('Calcule quanto você receberá de aumento e qual será o seu novo salário.')
sal = float(input('Salário atual: '))

if sal > 1250:
    a = sal * 0.10
    nsal = sal + a
else:
    a = sal * 0.15
    nsal = sal + a

print('Seu salário atual sendo {}, seu aumento será de {} e seu novo salário será R${}.'.format(sal, a, nsal))
