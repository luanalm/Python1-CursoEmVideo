# Exercício 24
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

nc = str(input('Nome de uma cidade: ')).strip()
nc = nc.upper()

if 'SANTO' in nc:
    nc.find('SANTO')
    if nc[:5] == 'SANTO':
        print('O nome da cidade começa com "Santo".')
    else:
        print('O nome da cidade tem "Santo", mas não começa por ele.')
else:
    print('O nome da cidade não possui "Santo" no nome.')
