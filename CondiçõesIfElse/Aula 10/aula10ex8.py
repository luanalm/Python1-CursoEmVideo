# Exercício 35
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

print('Verifique se três retas podem formar um triângulo.')
x = float(input('Reta 1: '))
y = float(input('Reta 2: '))
z = float(input('Reta 3: '))

cond1 = int(y - z) < x < (y + z)
cond2 = int(x - z) < y < (x + z)
cond3 = int(x - y) < z < (x + y)
cond = cond1 and cond2 and cond3

if cond:
    print('As retas formam um triângulo!')
else:
    print('As retas não formam um triângulo!')
