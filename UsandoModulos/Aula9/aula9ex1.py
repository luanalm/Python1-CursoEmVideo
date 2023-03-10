# Exercício 22
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome

nome = str(input('Nome completo: ')).strip()

let = (len(nome) - nome.count(' '))
s = nome.split()
snome = len(s[0])

print('Letras maiúsculas: {}'.format(nome.upper()))
print('Letras minúsculas: {}'.format(nome.lower()))
print('Quantas letras: {}'.format(let))
print('Letras primeiro nome: {}'.format(snome))
