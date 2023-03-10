# Exercício 25
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = str(input('Nome completo: ')).strip()
nome = nome.upper()

if 'SILVA' in nome:
    print('Há "Silva" no nome digitado')
else:
    print('Não há "Silva" no nome digitado')
