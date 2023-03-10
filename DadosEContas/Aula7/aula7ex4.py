# Exercício 7
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('Vamos calcular a média entre suas duas notas')
x = float(input('Primeira nota: '))
y = float(input('Segunda nota: '))

m = (x + y)/2

print('A média entre suas notas é {:.2f}'.format(m))
