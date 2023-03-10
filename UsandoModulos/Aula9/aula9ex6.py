# Exercício 27
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Exemplo: Ana Maria de Sousa. primeiro = Ana, último = Sousa.

nome = str(input('Nome completo: '))
nome.strip()

dn = nome.split()

print('O primeiro nome dessa pessa é {} e o seu último nome é {}'.format(dn[0], dn[-1]))
