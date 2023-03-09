from math import sqrt, floor
# se usar import math, antes da funcionalidade deve ser adicionado math.
# exemplo: math.sqrt

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raíz de {} é igual à {}'.format(num, floor(raiz)))

# math.ceil() arredonda o número para cima
# math.floor() aredonda o número para baixo
