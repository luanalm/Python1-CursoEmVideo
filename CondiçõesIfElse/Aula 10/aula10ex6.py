# Exercício 33
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('Por favor, escolha três números diferentes.')
x = int(input('Primeiro número: '))
y = int(input('Segundo número: '))
z = int(input('Terceiro número: '))

if (x > y) and (x > z):
    if y < z:
        print('Entre {}, {} e {}, o maior número é {} e o menor número é {}.'.format(x, y, z, x, y))
    else:
        print('Entre {}, {} e {}, o maior número é {} e o menor número é {}.'.format(x, y, z, x, z))
elif (y > x) and (y > z):
    if x < z:
        print('Entre {}, {} e {}, o maior número é {} e o menor número é {}.'.format(x, y, z, y, x))
    else:
        print('Entre {}, {} e {}, o maior número é {} e o menor número é {}.'.format(x, y, z, y, z))
elif (z > x) and (z > y):
    if x < y:
        print('Entre {}, {} e {}, o maior número é {} e o menor número é {}.'.format(x, y, z, z, x))
    else:
        print('Entre {}, {} e {}, o maior número é {} e o menor número é {}.'.format(x, y, z, z, y))
else:
    print('Há dois números iguais entre os números escolhidos.')
