# Exercício 16
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
# Ex: "Digite um número: 6.127. O número 6.127 tem a parte Inteira 6."

x = float(input('Escolha um número Real: '))

print('O número {}, tem a parte Inteira {}.'.format(x,int(x)))

# tem como resolver esse exercício usando math.trunc(x) no lugar de int(x)
