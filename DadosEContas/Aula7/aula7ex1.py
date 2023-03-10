n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro número: '))
so = n1 + n2
su = n1 - n2
mu = n1 * n2
di = n1 / n2
dint = n1 // n2
re = n1 % n2
po = n1 ** n2
print('\nA soma é {0}, \nA subtração é {1}, \nA multiplicação é {2}, \nA potenciação é {4}, \nA divisão é {3:.2f}, \n'.format(so, su, mu, di, po), end='')
print('A divisão inteira é {0} e o resto é {1}.'.format(dint, re))
