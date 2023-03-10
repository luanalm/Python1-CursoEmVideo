# Exercício 26
# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "a"
# - Em que posição específica ela aparece pela primeira vez
# - Em que posição ela aparece pela última vez

frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra "a" aparece na frase {} vezes'.format(frase.count('A')))
print('A primeira vez que a letra "a" aparece é na posição {}.'.format(frase.find('A')+1))
print('A última vez que a letra "a" aparece é na posição {}.'.format(frase.rfind('A')+1))
