# Escreva um programa que converta uma temperatura digitada em °C e converta para °F

print('Você deseja converter qual temperatura?')
x = int(input('Digite 0 para Celsius ou digite 1 para Fahrenheit: '))

if x == 0 :
    c = float(input('A temperatura em graus Celsius: '))
    f = (c*1.8)+32
    print('A temperatura em Fahrenheit é {:.1f}'.format(f))
elif x == 1:
    f = float(input('A temperatura em graus Fahrenheit: '))
    c = (f-32)/1.8
    print('A temperatura em Celsius é {:.1f}'.format(c))
else:
    print('O número escrito é inválido, tente novamente!')
    
