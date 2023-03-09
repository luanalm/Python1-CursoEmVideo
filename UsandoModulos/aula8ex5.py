# Exercício 20
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

a = input('Nome do primeiro aluno: ')
b = input('Nome do segundo aluno: ')
c = input('Nome do terceiro aluno: ')
d = input('Nome do quarto aluno: ')

lista = [a, b, c, d]

print('A ordem dos trabalho é {}'.format(shuffle(lista)))
