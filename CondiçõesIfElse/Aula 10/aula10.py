# tempo = int(input('Quantos anos tem o seu carro? '))

## Ao invés de usar o if dessa forma
# if tempo <= 3:
#     print('Carro novo')
# else:
#     print('Carro velho')
# print('Fim.')

## Em python, podemos usar ele dessa forma
# print('Carro novo'if tempo<=3 else 'Carro velho')
# print('Fim')

nome = str(input('Seu nome: ')).strip().upper()
if nome == 'LUANA':
    print('As melhores pessoas tem esse nome!')
print('Bom dia, {}!'.format(nome.title()))
